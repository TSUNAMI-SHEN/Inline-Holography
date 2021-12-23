class Config:
    training_lq = '../train_data/test/lq/'
    training_hq = '../train_data/test/hq/'

    data_path_test = '../cyro_em/test/norm/20211213/20211127-3/'
    data_path_checkpoint = '../cyro_em/model/20211214M/'          #保留训练模型的文件夹位置
    model_path_test = '../cyro_em/model/20211209W/denoise_epoch_200.pth'
    denoised_dir = '../cyro_em/denoised/20211209W-200epoch/20211127-3/'

    img_channel = 1
    max_epoch = 10
    crop_img_size = 640
    learning_rate = 0.0001
    save_per_epoch = 1
    cuda = "cuda:0"
    test_flag = False
