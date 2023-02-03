#pip install datasets

from datasets import Dataset
from datasets import load_dataset

dataset_dict = load_dataset("csv", data_files={"train": "download/tabular_regression/father_son_height/train.csv", "validation": "download/tabular_regression/father_son_height/validation.csv"})
#dataset_dict = load_dataset("json", data_files={"train": "download/tabular_regression/father_son_height/train.json", "validation": "download/tabular_regression/father_son_height/validation.json"})
#print(dataset_dict)
'''
DatasetDict({
    train: Dataset({
        features: ['Father', 'Son'],
        num_rows: 755
    })
    validation: Dataset({
        features: ['Father', 'Son'],
        num_rows: 323
    })
})
'''

train_dataset = dataset_dict['train']
validation_dataset = dataset_dict['validation']

#print(train_dataset)
'''
Dataset({
    features: ['Father', 'Son'],
    num_rows: 755
})
'''

for example in train_dataset:
    print(example['Father']) #165.1
    print(example['Son']) #151.892
    break
