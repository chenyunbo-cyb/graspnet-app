

""" Demo to show prediction results.
    Author: chenxi-wang
"""

import os
from re import T
import sys
import numpy as np
import open3d as o3d

import scipy.io as scio
from PIL import Image

num_point = 20000

# from .data_utils import CameraInfo, create_point_cloud_from_depth_image


class CameraInfo():
    """ Camera intrisics for point cloud creation. """

    def __init__(self, width, height, fx, fy, cx, cy, scale):
        self.width = width
        self.height = height
        self.fx = fx
        self.fy = fy
        self.cx = cx
        self.cy = cy
        self.scale = scale


def create_point_cloud_from_depth_image(depth, camera, organized=True):
    """ Generate point cloud using depth image only.

        Input:
            depth: [numpy.ndarray, (H,W), numpy.float32]
                depth image
            camera: [CameraInfo]
                camera intrinsics
            organized: bool
                whether to keep the cloud in image shape (H,W,3)

        Output:
            cloud: [numpy.ndarray, (H,W,3)/(H*W,3), numpy.float32]
                generated cloud, (H,W,3) for organized=True, (H*W,3) for organized=False
    """
    assert(depth.shape[0] == camera.height and depth.shape[1] == camera.width)
    xmap = np.arange(camera.width)
    ymap = np.arange(camera.height)
    xmap, ymap = np.meshgrid(xmap, ymap)
    points_z = depth / camera.scale
    points_x = (xmap - camera.cx) * points_z / camera.fx
    points_y = (ymap - camera.cy) * points_z / camera.fy
    cloud = np.stack([points_x, points_y, points_z], axis=-1)
    if not organized:
        cloud = cloud.reshape([-1, 3])
    return cloud


def get_and_process_data(data_dir):
    # load data
    color = np.array(Image.open(os.path.join(
        data_dir, 'color.png')), dtype=np.float32) / 255.0
    depth = np.array(Image.open(os.path.join(data_dir, 'depth.png')))
    workspace_mask = np.array(Image.open(
        os.path.join(data_dir, 'workspace_mask.png')))
    meta = scio.loadmat(os.path.join(data_dir, 'meta.mat'))
    
    intrinsic = meta['intrinsic_matrix']
    factor_depth = meta['factor_depth']

    # generate cloud
    camera = CameraInfo(
        1280.0, 720.0, intrinsic[0][0], intrinsic[1][1], intrinsic[0][2], intrinsic[1][2], factor_depth)
    cloud = create_point_cloud_from_depth_image(depth, camera, organized=True)
    print(workspace_mask.shape)

    # get valid points
    # mask = (workspace_mask & (depth > 0))
    mask = (workspace_mask & (depth > 0))
    cloud_masked = cloud[mask]
    color_masked = color[mask]

    # sample points
    if len(cloud_masked) >= num_point:
        idxs = np.random.choice(len(cloud_masked), num_point, replace=False)
    else:
        idxs1 = np.arange(len(cloud_masked))
        idxs2 = np.random.choice(
            len(cloud_masked), num_point-len(cloud_masked), replace=True)
        idxs = np.concatenate([idxs1, idxs2], axis=0)
    cloud_sampled = cloud_masked[idxs]
    color_sampled = color_masked[idxs]

    # convert data
    cloud = o3d.geometry.PointCloud()
    cloud.points = o3d.utility.Vector3dVector(cloud_sampled.astype(np.float32))
    cloud.colors = o3d.utility.Vector3dVector(color_sampled.astype(np.float32))

    return cloud



# ------------------------- 体素滤波 --------------------------
def TiSu(cloud): 
    print("->正在体素下采样...")
    voxel_size = 0.01
    downpcd = cloud.voxel_down_sample(voxel_size)
    # o3d.visualization.draw_geometries([cloud])
    print(downpcd)
    print("->正在可视化下采样点云")
    # o3d.visualization.draw_geometries([downpcd])
    return downpcd

# ------------------------- 统计滤波 --------------------------
# num_neighbors：用于指定邻域点的数量，以便计算平均距离。
# std_ratio：基于点云的平均距离的标准差来设置阈值。阈值越小，滤波效果越明显。
def TongJi(cloud):
    print("->正在进行统计滤波...")
    num_neighbors = 20 # K邻域点的个数
    std_ratio = 2.0 # 标准差乘数
    # 执行统计滤波，返回滤波后的点云sor_pcd和对应的索引ind
    sor_pcd, ind = cloud.remove_statistical_outlier(num_neighbors, std_ratio)
    sor_pcd.paint_uniform_color([0, 0, 1])
    print("统计滤波后的点云：", sor_pcd)

    sor_pcd.paint_uniform_color([0, 0, 1])
    # 提取噪声点云
    sor_noise_pcd = cloud.select_by_index(ind,invert = True)
    print("噪声点云：", sor_noise_pcd)
    sor_noise_pcd.paint_uniform_color([1, 0, 0])
    # # 可视化统计滤波后的点云和噪声点云
    return sor_pcd,sor_noise_pcd
    # o3d.visualization.draw_geometries([sor_pcd, sor_noise_pcd])
    # o3d.visualization.draw_geometries([cloud])

# ------------------------  平面分割 ------------------------  
# distance_threshold：inlier的最大距离阈值
# ransac_n：随机采样的平面点数
# num_iterations：表示最小迭代次数。
def PlaneOut(cloud):
    plane_model, inliers = cloud.segment_plane(distance_threshold=0.01,
                                         ransac_n=3,
                                         num_iterations=1000)
    # 模型参数
    [a, b, c, d] = plane_model
    print(f"Plane equation: {a:.2f}x + {b:.2f}y + {c:.2f}z + {d:.2f} = 0")
    # 平面内的点
    inlier_cloud = cloud.select_by_index(inliers)
    inlier_cloud.paint_uniform_color([1.0, 0, 0])
    # 平面外的点
    outlier_cloud = cloud.select_by_index(inliers, invert=True)
    # 可视化
    # o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud],
    #                                   zoom=0.8,
    #                                   front=[-0.4999, -0.1659, -0.8499],
    #                                   lookat=[2.1813, 2.0619, 2.0999],
    #                                   up=[0.1204, -0.9852, 0.1215])
    # o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])
    # TiSu(outlier_cloud)
    # o3d.visualization.draw_geometries([outlier_cloud])
    return inlier_cloud,outlier_cloud
    



 # ------------------------- 估计法线 -------------------------
def get_normal(cloud):
    print("->正在估计法线并可视化...")
    radius = 100  # 搜索半径
    max_nn = 200     # 邻域内用于估算法线的最大点数
    cloud.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius, max_nn))     # 执行法线估计
    o3d.visualization.draw_geometries([cloud], point_show_normal=True)

    print("->正在打印前10个点的法向量...")
    print(np.asarray(cloud.normals)[:10, :])



def demo(data_dir):
    # net = get_net()
    cloud = get_and_process_data(data_dir)
    # gg = get_grasps(net, end_points)
    # cloud = cloud.to_open3d_geometry_list()
  
    o3d.visualization.draw_geometries([cloud])
    PlaneOut(cloud)
    # TiSu(cloud)
    # TongJi(cloud)
    # get_normal(cloud)

    # 读取点云
    # pcd = o3d.io.read_point_cloud(point_cloud_file_path)

if __name__ == '__main__':
    data_dir='E:\graspnet\graspnet-baseline/doc/example_data/'
    demo(data_dir)
