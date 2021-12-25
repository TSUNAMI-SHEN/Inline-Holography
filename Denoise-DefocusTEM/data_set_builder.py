from __future__ import print_function, division
import os
import torch
from skimage import io
import numpy as np
import random
from torch.utils.data import DataLoader, Dataset
import torchvision.transforms.functional as tvF
import scipy.io as scio


class TrainingDataset(Dataset):

    def __init__(self, lq_image_dir, hq_image_dir):
        self.lq_image_dir = lq_image_dir
        self.hq_image_dir = hq_image_dir
        self.image_list = os.listdir(lq_image_dir)
        # self.image_size = image_size

    def __len__(self):
        return len(os.listdir(self.lq_image_dir))

    def __getitem__(self, idx):
        image_lq_path = os.path.join(self.lq_image_dir, self.image_list[idx])
        # img_even_in = io.imread(image_even_path)
        img_lq_in = scio.loadmat(image_lq_path)['F']

        image_hq_path = os.path.join(self.hq_image_dir, self.image_list[idx])
        # img_hq_in = io.imread(image_hq_path)
        img_hq_in = scio.loadmat(image_hq_path)['F']

        # h, w = img_lq_in.shape
        # new_h, new_w = self.image_size, self.image_size
        # top = np.random.randint(0, h-new_h+1)
        # left = np.random.randint(0, w-new_w+1)
        # cropped_even = img_even_in[top:top+new_h, left:left+new_w]
        # cropped_odd = img_odd_in[top:top+new_h, left:left+new_w]
        img_lq = np.expand_dims(img_lq_in, axis=-1)
        img_hq = np.expand_dims(img_hq_in, axis=-1)
        source = tvF.to_tensor(img_lq)  # 将矩阵自动转成[channel, height, width]格式
        target = tvF.to_tensor(img_hq)

        return source, target


class ValDataset(Dataset):
    ##only need to clean the even data
    def __init__(self, lq_image_dir, hq_image_dir):
        self.lq_image_dir = lq_image_dir
        self.hq_image_dir = hq_image_dir
        self.image_list = os.listdir(lq_image_dir)
        # self.image_size = image_size

    def __len__(self):
        return len(os.listdir(self.lq_image_dir))

    def __getitem__(self, idx):
        image_lq_path = os.path.join(self.lq_image_dir, self.image_list[idx])
        # img_even_in = io.imread(image_even_path)
        img_lq_in = scio.loadmat(image_lq_path)['F']
        image_hq_path = os.path.join(self.hq_image_dir, self.image_list[idx])
        # img_hq_in = io.imread(image_hq_path)
        img_hq_in = scio.loadmat(image_hq_path)['F']

        # h, w = img_lq_in.shape
        # new_h, new_w = self.image_size, self.image_size
        # top = np.random.randint(0, h-new_h+1)
        # left = np.random.randint(0, w-new_w+1)
        # cropped_even = img_even_in[top:top+new_h, left:left+new_w]
        # cropped_odd = img_odd_in[top:top+new_h, left:left+new_w]
        img_lq = np.expand_dims(img_lq_in, axis=-1)
        img_hq = np.expand_dims(img_hq_in, axis=-1)
        # source = torch.from_numpy(img_lq).float()
        # target = torch.from_numpy(img_hq).float()
        source = tvF.to_tensor(img_lq)  # 将矩阵自动转成[channel, height, width]格式
        target = tvF.to_tensor(img_hq)

        return source, target


class TestingDataset(Dataset):

    def __init__(self, image_dir):
        self.test_dir = image_dir
        self.test_list = os.listdir(image_dir)
        # self.test_image_size = image_size

    def __len__(self):
        return len(os.listdir(self.test_dir))

    def __getitem__(self, idx):
        image_name = os.path.join(self.test_dir, self.test_list[idx])
        # img = io.imread(image_name)
        img = scio.loadmat(image_name)['F']
        # input_temp = self.__crop_img(img)

        input_exdim = np.expand_dims(img, axis=-1)
        img_input = tvF.to_tensor(input_exdim)

        return img_input

    def __crop_img(self, img):
        """crop the image"""
        h, w = img.shape
        new_h, new_w = self.test_image_size, self.test_image_size
        top = np.random.randint(0, h - new_h + 1)
        left = np.random.randint(0, w - new_w + 1)
        cropped_img = img[top:top + new_h, left:left + new_w]
        return cropped_img
