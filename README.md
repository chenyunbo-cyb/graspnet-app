# GraspNet Baseline
Baseline model for "GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping" (CVPR 2020).

[[paper](https://openaccess.thecvf.com/content_CVPR_2020/papers/Fang_GraspNet-1Billion_A_Large-Scale_Benchmark_for_General_Object_Grasping_CVPR_2020_paper.pdf)]
[[dataset](https://graspnet.net/)]
[[API](https://github.com/graspnet/graspnetAPI)]
[[doc](https://graspnetapi.readthedocs.io/en/latest/index.html)]

<div align="center">    
    <img src="https://github.com/chenxi-wang/materials/blob/master/graspnet-baseline/doc/gifs/scene_0114.gif", width="240", alt="scene_0114" />
    <img src="https://github.com/chenxi-wang/materials/blob/master/graspnet-baseline/doc/gifs/scene_0116.gif", width="240", alt="scene_0116" />
    <img src="https://github.com/chenxi-wang/materials/blob/master/graspnet-baseline/doc/gifs/scene_0117.gif", width="240", alt="scene_0117" />
    <br> Top 50 grasps detected by our baseline model.
</div>

![teaser](doc/teaser.png)

## PyQt application
抓取位姿估计系统的体系结构主要分为四层，即数据输入层、数据预处理层、算法处理层和结果输出层。系统的层次结构如图所示。
 ![image](https://github.com/chenyunbo-cyb/graspnet-app/assets/52398597/775c7c64-859c-4fe2-b0cd-0060fa44c354)

### 加载点云数据模块界面
 ![image](https://github.com/chenyunbo-cyb/graspnet-app/assets/52398597/aed84b80-a1fe-4ba2-9e97-c411e6cd8ab5)
### 打开点云文件
 ![image](https://github.com/chenyunbo-cyb/graspnet-app/assets/52398597/3d57c6ca-c417-4d9b-a545-32225397eecd)

### 点云显示界面
 ![image](https://github.com/chenyunbo-cyb/graspnet-app/assets/52398597/b6c6799b-537f-449f-8cd4-28f71259c7b6)
![image](https://github.com/chenyunbo-cyb/graspnet-app/assets/52398597/976c1eae-a573-4705-a821-73a9caf6297b)

### 点云预处理模块
![image](https://github.com/chenyunbo-cyb/graspnet-app/assets/52398597/eac74ffd-d162-42c3-9f62-d3569de9d609)
 
### 统计滤波结果
![image](https://github.com/chenyunbo-cyb/graspnet-app/assets/52398597/2ef99512-9cca-4c66-8403-90b5d118b1ab)

 
### 提取平面结果
![image](https://github.com/chenyunbo-cyb/graspnet-app/assets/52398597/a4cbf964-fad9-4645-8097-183f9777acd8)

 
### 平面分割结果

![image](https://github.com/chenyunbo-cyb/graspnet-app/assets/52398597/c6436777-5f46-4e8b-91ea-af6cb0ef749a)


### 体素降采样结果
![image](https://github.com/chenyunbo-cyb/graspnet-app/assets/52398597/b4d8b4e7-78d6-4a71-8e1e-d1cdd67be32f)

### 估计抓取位姿模块
 
### 估计抓取位姿模块界面
 ![image](https://github.com/chenyunbo-cyb/graspnet-app/assets/52398597/b90d2e6a-6782-478c-b719-87d5abee7ca0)

### 抓取位姿信息输出结果
 ![image](https://github.com/chenyunbo-cyb/graspnet-app/assets/52398597/00f94020-6ab8-41dd-b7e2-ba5bb6a9c45e)
 
### 抓取位姿可视化
![image](https://github.com/chenyunbo-cyb/graspnet-app/assets/52398597/99b3580e-a8b0-4142-b6ab-b9942c213296)



## Requirements
- Python 3
- PyTorch 1.6
- Open3d >=0.8
- TensorBoard 2.3
- NumPy
- SciPy
- Pillow
- tqdm

## Installation
Get the code.
```bash
git clone https://github.com/graspnet/graspnet-baseline.git
cd graspnet-baseline
```
Install packages via Pip.
```bash
pip install -r requirements.txt
```
Compile and install pointnet2 operators (code adapted from [votenet](https://github.com/facebookresearch/votenet)).
```bash
cd pointnet2
python setup.py install
```
Compile and install knn operator (code adapted from [pytorch_knn_cuda](https://github.com/chrischoy/pytorch_knn_cuda)).
```bash
cd knn
python setup.py install
```
Install graspnetAPI for evaluation.
```bash
git clone https://github.com/graspnet/graspnetAPI.git
cd graspnetAPI
pip install .
```

## Tolerance Label Generation
Tolerance labels are not included in the original dataset, and need additional generation. Make sure you have downloaded the orginal dataset from [GraspNet](https://graspnet.net/). The generation code is in [dataset/generate_tolerance_label.py](dataset/generate_tolerance_label.py). You can simply generate tolerance label by running the script: (`--dataset_root` and `--num_workers` should be specified according to your settings)
```bash
cd dataset
sh command_generate_tolerance_label.sh
```

Or you can download the tolerance labels from [Google Drive](https://drive.google.com/file/d/1DcjGGhZIJsxd61719N0iWA7L6vNEK0ci/view?usp=sharing)/[Baidu Pan](https://pan.baidu.com/s/1HN29P-csHavJF-R_wec6SQ) and run:
```bash
mv tolerance.tar dataset/
cd dataset
tar -xvf tolerance.tar
```

## Training and Testing
Training examples are shown in [command_train.sh](command_train.sh). `--dataset_root`, `--camera` and `--log_dir` should be specified according to your settings. You can use TensorBoard to visualize training process.

Testing examples are shown in [command_test.sh](command_test.sh), which contains inference and result evaluation. `--dataset_root`, `--camera`, `--checkpoint_path` and `--dump_dir` should be specified according to your settings. Set `--collision_thresh` to -1 for fast inference.

The pretrained weights can be downloaded from:

- `checkpoint-rs.tar`
[[Google Drive](https://drive.google.com/file/d/1hd0G8LN6tRpi4742XOTEisbTXNZ-1jmk/view?usp=sharing)]
[[Baidu Pan](https://pan.baidu.com/s/1Eme60l39tTZrilF0I86R5A)]
- `checkpoint-kn.tar`
[[Google Drive](https://drive.google.com/file/d/1vK-d0yxwyJwXHYWOtH1bDMoe--uZ2oLX/view?usp=sharing)]
[[Baidu Pan](https://pan.baidu.com/s/1QpYzzyID-aG5CgHjPFNB9g)]

`checkpoint-rs.tar` and `checkpoint-kn.tar` are trained using RealSense data and Kinect data respectively.

## Demo
A demo program is provided for grasp detection and visualization using RGB-D images. You can refer to [command_demo.sh](command_demo.sh) to run the program. `--checkpoint_path` should be specified according to your settings (make sure you have downloaded the pretrained weights). The output should be similar to the following example:

<div align="center">    
    <img src="doc/example_data/demo_result.png", width="480", alt="demo_result" />
</div>

__Try your own data__ by modifying `get_and_process_data()` in [demo.py](demo.py). Refer to [doc/example_data/](doc/example_data/) for data preparation. RGB-D images and camera intrinsics are required for inference. `factor_depth` stands for the scale for depth value to be transformed into meters. You can also add a workspace mask for denser output.

## Results
Results "In repo" report the model performance with single-view collision detection as post-processing. In evaluation we set `--collision_thresh` to 0.01.

Evaluation results on RealSense camera:
|          |        | Seen             |                  |        | Similar          |                  |        | Novel            |                  | 
|:--------:|:------:|:----------------:|:----------------:|:------:|:----------------:|:----------------:|:------:|:----------------:|:----------------:|
|          | __AP__ | AP<sub>0.8</sub> | AP<sub>0.4</sub> | __AP__ | AP<sub>0.8</sub> | AP<sub>0.4</sub> | __AP__ | AP<sub>0.8</sub> | AP<sub>0.4</sub> |
| In paper | 27.56  | 33.43            | 16.95            | 26.11  | 34.18            | 14.23            | 10.55  | 11.25            | 3.98             |
| In repo  | 47.47  | 55.90            | 41.33            | 42.27  | 51.01            | 35.40            | 16.61  | 20.84            | 8.30             |

Evaluation results on Kinect camera:
|          |        | Seen             |                  |        | Similar          |                  |        | Novel            |                  | 
|:--------:|:------:|:----------------:|:----------------:|:------:|:----------------:|:----------------:|:------:|:----------------:|:----------------:|
|          | __AP__ | AP<sub>0.8</sub> | AP<sub>0.4</sub> | __AP__ | AP<sub>0.8</sub> | AP<sub>0.4</sub> | __AP__ | AP<sub>0.8</sub> | AP<sub>0.4</sub> |
| In paper | 29.88  | 36.19            | 19.31            | 27.84  | 33.19            | 16.62            | 11.51  | 12.92            | 3.56             |
| In repo  | 42.02  | 49.91            | 35.34            | 37.35  | 44.82            | 30.40            | 12.17  | 15.17            | 5.51             |

## Citation
Please cite our paper in your publications if it helps your research:
```
@inproceedings{fang2020graspnet,
  title={GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping},
  author={Fang, Hao-Shu and Wang, Chenxi and Gou, Minghao and Lu, Cewu},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition(CVPR)},
  pages={11444--11453},
  year={2020}
}
```

## License
All data, labels, code and models belong to the graspnet team, MVIG, SJTU and are freely available for free non-commercial use, and may be redistributed under these conditions. For commercial queries, please drop an email at fhaoshu at gmail_dot_com and cc lucewu at sjtu.edu.cn .
