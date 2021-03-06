import torch
import torch.nn as nn
from torch.optim import Adam, lr_scheduler
import os
import torchvision.transforms.functional as tvF
from unet_model import UNet
from Config import Config as conf
from data_set_builder import TestingDataset
from torch.utils.data import Dataset, DataLoader
import scipy.io as scio

# 训练好的模型用于离焦图像降噪
def test():
    device = torch.device(conf.cuda if torch.cuda.is_available() else "cpu")
    test_dataset = TestingDataset(conf.data_path_test)
    test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False)
    print('Loading model from: {}'.format(conf.model_path_test))
    model = UNet(in_channels=conf.img_channel, out_channels=conf.img_channel)
    model = nn.DataParallel(model)
    print('Loading Model')
    # checkpoint = torch.load(conf.model_path_test)
    model.load_state_dict(torch.load(conf.model_path_test, map_location='cuda:0')['model'])
    model.eval()

    model.to(device)
    result_dir = conf.denoised_dir
    if not os.path.exists(result_dir):
        os.mkdir(result_dir)
    for batch_idx, source in enumerate(test_loader):
        source = source.to(device)
        denoised_img = model(source).detach().cpu()  # 将矩阵从gpu转移到cpu上
        denoised_img = denoised_img.numpy()  # 将tensor转换成ndarray，此时ndarray维度为[1,1,512,512]
        denoised_img = denoised_img.reshape(512, 512)  # 将ndarray维度转换成[512, 512]
        img_name = test_loader.dataset.test_list[batch_idx]
        fname = os.path.splitext(img_name)[0]
        target_path = os.path.join(result_dir, f'{fname}.mat')
        scio.savemat(target_path, {'F': denoised_img})  # mat格式保留矩阵数据


def main():
    test()


if __name__ == '__main__':
    main()
