#하이퍼파라미터 튜닝을 위해 실행시 마다 변수가 같은 초기값 가지게 하기 시작
import torch
random_seed = 777
torch.manual_seed(random_seed) #torch의 random seed 고정
torch.backends.cudnn.deterministic = True #CuDNN(딥러닝에 특화된 CUDA library)의 random seed 고정
torch.backends.cudnn.benchmark = False #
import numpy as np
np.random.seed(random_seed) #numpy의 random seed 고정
import random
random.seed(random_seed)  #random의 random seed 고정
#하이퍼파라미터 튜닝을 위해 실행시 마다 변수가 같은 초기값 가지게 하기 끝
import pandas as pd
import torch
import os
#from fastai.vision.all import *
from torch.nn import functional as F
from torchsummaryX import summary
from datasets import load_dataset, Dataset
#from model import *

raw_dataset_dict = load_dataset("csv", data_files={"train": "download/tabular_regression/father_son_height/train.csv", "validation": "download/tabular_regression/father_son_height/validation.csv"})
raw_train_dataset = raw_dataset_dict['train']
raw_validation_dataset = raw_dataset_dict['validation']

class SonHeightDataset(torch.utils.data.Dataset):
    def __init__(self, raw_dataset):
        self.raw_dataset = raw_dataset

    def __len__(self):
        return len(self.raw_dataset)

    def __getitem__(self, index):
        example = self.raw_dataset[index]
        x = example['Father']
        x = np.array([x], dtype=np.float32)
        labels = example['Son']
        labels = np.array([labels], dtype=np.float32)
        return x, labels

train_dataset = SonHeightDataset(raw_train_dataset)
validation_dataset = SonHeightDataset(raw_validation_dataset)


train_data_loader = torch.utils.data.DataLoader(train_dataset, batch_size=32, shuffle=True)
validation_data_loader = torch.utils.data.DataLoader(validation_dataset, batch_size=32, shuffle=False)

lr = 0.01 #Adam lr 의 디폴트 0.001, transformers.TrainingArguments learning_rate 의 디폴트 0.00005
optimizer = torch.optim.Adam(model.parameters(), lr=lr)
scheduler = torch.optim.lr_scheduler.LinearLR(optimizer, start_factor=0.3333333333333333, total_iters=5)

epochs = 30 #디폴트 30

for epoch_index in range(epochs):
    accumulated_loss = 0
    batch_count = 0
    for batch in train_data_loader:
        x, y = batch
