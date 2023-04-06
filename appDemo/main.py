# -*- coding: utf-8 -*-
import imp
import sys
from PyQt5.QtWidgets import QApplication, QDialog
import sys,os

# 加载PyQt的函数库
from PyQt5 import QtWidgets
from Ui_untitled import Ui_Form  # 加载绘制的UI界面
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QLabel, QInputDialog, QLineEdit # 弹出提示窗
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication    # 二维图片preprocess数据显示
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer, QObject,pyqtSignal
import qdarkstyle

import pyqtgraph.opengl as gl
import pyqtgraph as pg  # 二维曲线绘图

import open3d as o3d
import numpy as np  # 数据处理的库 numpy

import preprocess
# from .. import demo

import sys
print(sys.path)
sys.path.append('E:\graspnet\graspnet-baseline')
sys.path.append('E:\graspnet\graspnet-baseline\appDemo')
# sys.path.append('E:\graspnet\graspnet-baseline\demo.py')

import demo

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     MainWindow = QtWidgets()
#     ui = untitled.Ui_Form()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())


class MyPyQT_Form(QtWidgets.QWidget, Ui_Form):  # 系统主界面
    def __init__(self):
        super(MyPyQT_Form, self).__init__()
        self.timer_camera = QTimer(self)
        self.setupUi(self)
        # pixmap = QPixmap("E:\graspnet\graspnet-baseline\doc\example_data\color.png")         # 按指定路径找到图片，注意路径必须用双引号包围，不能用单引号
        # self.label.setPixmap(pixmap)                                                  # 在label上显示图片
        # self.label.setScaledContents(True)                                            # 让图片自适应label大小
        self.initUI()
        # self.initOpen3d()
        self.initFuntion()


    def onUpdateText(self, text):
        """Write console output to text widget."""
        cursor = self.process.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.process.setTextCursor(cursor)
        self.process.ensureCursorVisible()


    def initUI(self):
        # TODO:初始化将所有的界面，全部置为首页显示
        # self.stackedWidget.setCurrentIndex(0)
        # self.stackedWidget_2.setCurrentIndex(0)
        
        print("OK")


    def initFuntion(self):
        # self.image_dir = os.path.join(os.getcwd(), "image")
        # TODO:定义点云的openGL显示窗口
        opengl_weight = gl.GLViewWidget()
        opengl_weight.opts['distance'] = 20
        self.horizontalLayout_2.addWidget(opengl_weight)
        # self.horizontalLayout_5.addWidget(opengl_weight)
        opengl_weight.setWindowTitle('pyqtgraph example: GLScatterPlotItem')

        
        gl_glgrideitem = gl.GLGridItem()  # 添加网格
        opengl_weight.addItem(gl_glgrideitem)
        gl_axis = gl.GLAxisItem()   # 添加xyz坐标轴
        opengl_weight.addItem(gl_axis)

        self.sp2 = gl.GLScatterPlotItem(pos=None, color=(1, 1, 1, 1), size=2)  # 不带有任何颜色的白点
        # phase = 0.
        opengl_weight.addItem(self.sp2)

    def initFuntion_1(self):
        # self.image_dir = os.path.join(os.getcwd(), "image")
        # TODO:定义点云的openGL显示窗口
        opengl_weight = gl.GLViewWidget()
        opengl_weight.opts['distance'] = 20
        # self.horizontalLayout_2.addWidget(opengl_weight)
        self.horizontalLayout_5.addWidget(opengl_weight)
        opengl_weight.setWindowTitle('pyqtgraph example: GLScatterPlotItem')

        
        gl_glgrideitem = gl.GLGridItem()  # 添加网格
        opengl_weight.addItem(gl_glgrideitem)
        gl_axis = gl.GLAxisItem()   # 添加xyz坐标轴
        opengl_weight.addItem(gl_axis)

        self.sp3 = gl.GLScatterPlotItem(pos=None, color=(1, 1, 1, 1), size=2)  # 不带有任何颜色的白点
        # phase = 0.
        opengl_weight.addItem(self.sp3)

####################################################################################
# Define some methods
####################################################################################
    def pointcloud_File_open(self):
        print("pointcloud_open is loading...")
        # self.programe_threading_quit()
        # self.programe_timer_quit()

        try:
            fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                    "选取文件",
                                                                    os.getcwd(),  # 起始路径
                                                                    "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,用双分号间
        except:
            fileName_choose = ""
            QMessageBox.critical(self, "waring", "系统未检测到任何文件")
        
        print(fileName_choose)
        file_type = fileName_choose.split(".")[-1] 
      
        if file_type == 'pcd':
            # 读取点云
            pcd = o3d.io.read_point_cloud(fileName_choose)
            # 获取 Numpy 数组
            np_points = np.asarray(pcd.points)

            points_pcd_sig = np_points[:, 0:3]
            pc_inte = np_points[:, 2] 
            # pc_color = self.pointcloud_inte_to_rgb(pc_inte)

            self.sp2.setData(pos=points_pcd_sig, color=(0, 0, 1, 1), size=0.0005, pxMode=False)   
            # self.sp2.setData(pos=points_pcd_sig, color=pc_color, size=0.0005, pxMode=False)
   

        elif fileName_choose.split(".")[-1] == 'npy':
            try:
                np.set_printoptions(suppress=True) # 取消默认科学计数法，open3d无法读取科学计数法表示
                data = np.load(fileName_choose)
                np.savetxt('D:\Desktop\datasets\ycb_grasp/train/txt/1.txt', data)
                # 读取点云并可视化
                pcd =o3d.io.read_point_cloud('D:\Desktop\datasets\ycb_grasp/train/txt/1.txt', format='xyz') # 原npy文件中的数据正好是按x y z r g b进行排列
                print(pcd)
                o3d.visualization.draw_geometries([pcd], width=600, height=600)
                # o3d.visualization.draw_geometries([pcd])

                # points_list = np.load(fileName_choose)
                # print(points_list.shape)  # (6500, 12)
                # points_npy = np.array(points_list, dtype=np.float32)
                # print(points_npy.shape)  # (6500, 12)
                # points_npy_sig = points_npy[:, 0:3]
                # pc_inte = points_npy[:, 2]
                # pc_color = self.pointcloud_inte_to_rgb(pc_inte)
                # self.sp2.setData(pos=points_npy_sig, color=pc_color)
            except:
                QMessageBox.critical(self, "waring", "文件打开失败，请选择正确的npy文件！！")

        else:
            QMessageBox.critical(self, "waring", "不支持的文件类型")

    
    # data_dir = ''
    def pointcloud_Directory_open(self):
        """
        :打开有RGBD图片的文件夹，生成并返回点云数据
        :param :
        :return: cloud

        """
        print("pointclouud_target_recognition_algorithm is loading...")
        self.label.setText("正在打开文件夹")
        try:
            data_dir  = QFileDialog.getExistingDirectory(self,"选取文件夹", "E:\graspnet\graspnet-baseline\doc")  # 设置文件扩展名过滤,用双分号间
            print("try ok")
        except:
            data_dir = ""
            QMessageBox.critical(self, "waring", "系统未检测到任何文件")

        print(data_dir)
        self.label.setText("打开文件夹："+data_dir)
        cloud = preprocess.get_and_process_data(data_dir)
        return cloud       



    def pointcloud_Directory_open_view(self):

        cloud = self.pointcloud_Directory_open()
        def rotate_view(vis):
            ctr = vis.get_view_control()
            ctr.rotate(10.0, 0.0)
            return False       
        o3d.visualization.draw_geometries_with_animation_callback([cloud],
                                                               rotate_view, width=600, height=600)
        
        # o3d.visualization.draw_geometries([cloud], width=600, height=600)
        # o3d.visualization.draw_geometries([cloud])
        # 
        #        
        # vis = o3d.visualization.Visualizer()
        # vis.create_window()
        # vis.add_geometry(cloud)
        # o3d.visualization.ViewControl.set_zoom(vis.get_view_control())
        # vis.run()

        print(cloud)
        self.label.setText("显示成功")


    def pointcloud_plane_get(self):
        """
        :提取平面
        :param : 
        :return: 
        """ 
        print("pointcloud_plane_get is loading...")
        self.label.setText("准备提取平面...")
        # if data_dir == '':
        #     QMessageBox.critical(self, "waring", "系统未检测到任何文件")
        # else:
        #     cloud = preprocess.get_and_process_data(data_dir)
        cloud = self.pointcloud_Directory_open()
        # pcd = o3d.io.read_point_cloud("E:\graspnet\graspnet-baseline\doc/table_scene_lms400.pcd")
        inlier_cloud,outlier_cloud = preprocess.PlaneOut(cloud) 
        # o3d.visualization.draw_geometries([inlier_cloud,outlier_cloud], width=600, height=600)
        # o3d.visualization.draw_geometries([inlier_cloud,outlier_cloud])
        def rotate_view(vis):
            ctr = vis.get_view_control()
            ctr.rotate(10.0, 0.0)
            return False       
        o3d.visualization.draw_geometries_with_animation_callback([inlier_cloud,outlier_cloud],
                                                               rotate_view, width=600, height=600)

        print("平面提取完成！")




    def pointcloud_plane_delete(self):
        print("pointcloud_plane_delete is loading...")
        self.label.setText("准备分割平面")
        cloud = self.pointcloud_Directory_open()

        inlier_cloud,outlier_cloud = preprocess.PlaneOut(cloud)
        # o3d.visualization.draw_geometries([outlier_cloud], width=600, height=600)
        def rotate_view(vis):
            ctr = vis.get_view_control()
            ctr.rotate(10.0, 0.0)
            return False       
        o3d.visualization.draw_geometries_with_animation_callback([outlier_cloud],
                                                               rotate_view, width=600, height=600)

    
        print("平面分割完成")

    def pointcloud_TS_Filtering(self):
        print(" pointcloud_mutil_frame_open  ")
        self.label.setText("体素滤波进行中...")
        cloud = self.pointcloud_Directory_open()

        cloud = preprocess.TiSu(cloud)
        # o3d.visualization.draw_geometries([cloud], width=600, height=600)
        def rotate_view(vis):
            ctr = vis.get_view_control()
            ctr.rotate(10.0, 0.0)
            return False       
        o3d.visualization.draw_geometries_with_animation_callback([cloud],
                                                               rotate_view, width=600, height=600)

        print("体素滤波完成")

        

    def pointcloud_TJ_Filtering(self):
        print(" pointcloud_mutil_frame_open  ")
        self.label.setText("统计滤波进行中..")
        cloud = self.pointcloud_Directory_open()

        sor_pcd,sor_noise_pcd = preprocess.TongJi(cloud)
        # o3d.visualization.draw_geometries([sor_pcd,sor_noise_pcd], width=600, height=600)
        def rotate_view(vis):
            ctr = vis.get_view_control()
            ctr.rotate(10.0, 0.0)
            return False       
        o3d.visualization.draw_geometries_with_animation_callback([sor_pcd,sor_noise_pcd],
                                                               rotate_view, width=600, height=600)

        # self.label.setText("噪声点云：sor_noise_pcd")
        print("统计滤波完成")

    def grasp_print(self):
        print(" grasp_print  ")
        # QMessageBox.critical(self, "warning", "功能开发中...")
        data_dir = 'E:\graspnet\graspnet-baseline\doc'
        gg,cloud = demo.demo(data_dir)

        self.textEdit.setPlainText(str(gg))
        # print(gg)
        grippers = gg.to_open3d_geometry_list()     
        # o3d.visualization.draw_geometries_with_animation_callback([cloud, *grippers],rotate_view, window_name='抓取位姿结果可视化',width=800, height=800)
        o3d.visualization.draw_geometries([cloud, *grippers],width=800, height=800)       

        

    def grasp_view(self):
        print(" grasp_view  ")
        QMessageBox.critical(self, "warning", "功能开发中...")
        # data_dir = 'doc/example_data'
        # demo.demo(data_dir)

        # self.label.setText("噪声点云：sor_noise_pcd")
        # print("统计滤波完成")
  
    def closeEvent(self, event):
        """
        参考：https://www.cnblogs.com/foreverlin/p/10881346.html
        对MainWindow的函数closeEvent进行重构
        退出软件时结束所有进程
        :param event:
        :return:
        """
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            self.programe_threading_quit()
            self.programe_timer_quit()
            os._exit(0)
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())     # 使用开源插件优化界面

    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()

    sys.exit(app.exec_())