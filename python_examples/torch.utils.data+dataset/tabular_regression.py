#pip install datasets
#pip install pytorch

from datasets import load_dataset
import torch

raw_dataset_dict = load_dataset("csv", data_files={"train": "custom-datasets/tabular_regression/father_son_height/train.csv", "validation": "custom-datasets/tabular_regression/father_son_height/validation.csv"})
raw_train_dataset = raw_dataset_dict['train']
raw_validation_dataset = raw_dataset_dict['validation']

class SonHeightDataset(torch.utils.data.Dataset):
    def __init__(self, raw_dataset):
        self.raw_dataset = raw_dataset

    def __len__(self):
        return len(self.raw_dataset)

    def __getitem__(self, index):
        example = self.raw_dataset[index]
        return example['Father'], example['Son']

train_dataset = SonHeightDataset(raw_train_dataset)
validation_dataset = SonHeightDataset(raw_validation_dataset)

for example in train_dataset:
    Father, Son = batch
    print(Father) #165.1
    print(Son) #151.892
    break
