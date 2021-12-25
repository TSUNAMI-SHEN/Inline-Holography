用于离焦电镜图像降噪

1.脚本说明
    
    1.test.py : 利用训练好的U-Net网络模型对离焦的电镜图像进行降噪, 该脚本不需要修改

    2.Config.py : 存储相关参数，其中测试时需要修改的有三个参数

        参数1：data_path_test ： 原始离焦图像保存的文件夹路径
    
        参数2：model_path_test : 选择用哪一个训练好的神经网络模型
    
        参数3：denoised_dir ：保存降噪后离焦图像的文件夹路径
        
    3.unet_model.py : U-Net模型，测试时test.py会调用该模型，无需修改
    
    4.data_set_builder.py : 用于加载数据，测试时test.py会调用该脚本，无需修改
    
2.注意事项
    
    1.训练前，需要将矩阵截成512 * 512大小输入，并利用normI.m脚本对矩阵进行normalize

    2.配置环境&安装包版本&GPU信息

        Python = 3.6
        torch = 1.2.0
        scipy = 1.5.2
        scikit-image = 0.17.2
        torchvision = 0.4.0
        numpy = 1.17.0
        cuda = 10.0
        cudnn = 7.4.1
