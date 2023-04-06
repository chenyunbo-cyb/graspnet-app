# GraspNetAPI example for visualization.
# change the graspnet_root path
####################################################################
graspnet_root = 'F:\\BaiduNetdiskDownload\\train_1'      # ROOT PATH FOR GRASPNET
####################################################################
from graspnetAPI import GraspNet

# 1. initialize a GraspNet instance  
g = GraspNet(graspnet_root, camera='kinect', split='train')

# 2.1 show object grasps
g.showObjGrasp(objIds = 1, show=True)


        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(Form.pointcloud_File_open)
        self.pushButton_2.clicked.connect(Form.pointcloud_Directory_open_view)

        self.pushButton_3.clicked.connect(Form.pointcloud_plane_get)
        self.pushButton_4.clicked.connect(Form.pointcloud_plane_delete)

        self.pushButton_5.clicked.connect(Form.pointcloud_TS_Filtering)
        self.pushButton_6.clicked.connect(Form.pointcloud_TJ_Filtering)

        self.pushButton_7.clicked.connect(Form.grasp_view)
        self.pushButton_8.clicked.connect(Form.grasp_print)