Inline的整个流程

main.m脚本中调用每个流程封装的函数，下面是调用函数时需要输入参数以及输出的说明

主要程序分成三大模块

    第一个模块是读取数据，并对数据进行预处理

      1.DMToMat.m 函数
  
        输入参数
    
          1.foldername : 原始电镜文件保存的位置, str类型
      
          2.filetype : 文件的类型，dm3 or dm4 or txt等（目前的脚本仅针对dm3文件，需要后面完善）, str类型
      
          3.output : 输出文件的文件夹名称, str类型
      
        输出：系列离焦像的矩阵，mat格式
    
      2.Autoalign.m 函数
  
        输入参数
      
          1.foldername : mat格式离焦像保存的文件夹名称, str类型
      
          2.output : 输出文件的文件夹名称, str类型
      
          3.colorbarmin : 显示离焦图像时colorbar的下限，float类型，根据矩阵的像素值大小而定
      
          4.colorbarmax : 显示离焦图像时colorbar的上限，float类型，根据矩阵的像素值大小而定
      
          5.sizee : 需要截取区域边长的一半（如sizee=100，则返回200*200的矩阵），int类型
      
          6.cut : 从高到底截取互相关系数的数量，即取前cut个互相关系数（降序排列好的），通过调节cut来调整对准的效果，int类型
      
        输出 : 对准好的离焦图像，保存为mat格式
  
      3.Padding.m 函数
    
        输入参数
      
          1.foldername : 对准好的离焦图像所在的文件夹名称, str类型
      
          2.output : 填充好的离焦图像保存的文件夹名称, str类型
      
          3.DUpli : 周围填充的像素点数量, int类型
    
        输出 : 填充好且对准的离焦图像，mat格式
  
    第二个模块是利用迭代脚本重构波函数
        
        GPU_RePhase_FRWR_edge_N.m 函数
          
          输入参数
            
            1.foldername : 第一模块中对准且填充好的离焦图像所在的文件夹名称, str类型
            
            2.output : 保存相关结果的文件夹名称, str类型
            
            3.defocus_step : 离焦步长，单位是nm, int类型
            
            4.flag : 区分过焦or欠焦，填1或-1，1-过焦，-1-欠焦
            
            5.stepxy : 像素点的大小，单位是nm, float类型，由dm文件获取
            
            6.term : 迭代的次数，int类型
            
            7.E : 电镜的加速电压，单位是kV，int类型
          
          输出
            
            1.bmp文件，模拟的振幅图&正焦的相位图
            
            2.conv_0.mat，收敛曲线
            
            3.Fs.mat，存储波函数的矩阵，其中GPU_F0是不同离焦面的波函数，需要用到
      
    第三个模块是利用波函数相位信息计算泊松方程，求电荷分布信息
        
        1.ChargeGet.m 函数
          
          输入参数
            
            1.filename : 波函数矩阵的路径及文件名，str类型
            
            2.output : 保存电荷分布矩阵的文件夹名称，str类型
            
            3.sizeex : 截取感兴趣区域的x边长的1/2，int类型
            
            4.sizey : 截取感兴趣区域的y边长的1/2，int类型
            
            5.stepxy : 像素点大小，单位是nm，float类型，由dm文件获取
            
            6.E : 电镜的加速电压，单位是kV，int类型
            
            7.n : 高斯平滑的次数，int类型
            
            8.kernel : 高斯平滑的核大小，int类型
            
            9.sigmal : 高斯核的方差，int类型
            
          输出
            
            1.Origin-CM.mat，未经平滑的原始电荷分布结果
            
            2.Smooth-CM.mat，平滑后的电荷分布结果
            
            3.Phase.mat, 相位结果
  辅助模块，用于保存图像、预览电荷分布结果、相位
    
    1.SaveImg.m 函数，用来保存灰度图，保存
      
      输入参数
        
        1.foldername : mat格式离焦图像保存的文件夹名称，str类型
        
        2.output : 保存离焦图像的文件夹名称，str类型
        
        3.scale : 调整保存图像的亮度，float类型，越大，图像的亮度越大
      
      输出 : tif格式的离焦图像
    
    2.PreviewGray.m 函数，用于预览灰度图
      
      输入参数
        
        1.foldername : mat文件所在的文件夹名称, str类型
        
        2.colorbarmin : colorbar的下限，float类型，根据矩阵的像素值大小而定
        
        3.colorbarmax : colorbar的上限，float类型，根据矩阵的像素值大小而定
        
      输出 : 显示灰度图像
    
    3.PreviewRGB.m 函数，用于预览电荷分布等RGB图
    
      输入参数
        
        1.foldername : mat文件所在的文件夹名称, str类型
        
        2.colorbarmin : colorbar的下限，float类型，根据矩阵的像素值大小而定
        
        3.colorbarmax : colorbar的上限，float类型，根据矩阵的像素值大小而定
      
      输出 : 显示RGB图像
