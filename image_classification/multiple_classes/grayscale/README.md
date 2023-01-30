
download from github

<pre>
!git clone https://github.com/automatethem/download
</pre>

python example

<pre>
from datasets import Dataset
from datasets import load_dataset

'''
dataset_dict = load_dataset("json", data_files={"train": "download/image_classification/multiple_classes/grayscale/json/train.json", "validation": "download/image_classification/multiple_classes/grayscale/json/validation.json"})
#print(dataset_dict)
#DatasetDict({
#    train: Dataset({
#        features: ['image', 'label'],
#        num_rows: 32
#    })
#    validation: Dataset({
#        features: ['image', 'label'],
#        num_rows: 8
#    })
#})

train_dataset = dataset_dict['train']
validation_dataset = dataset_dict['validation']

#print(train_dataset)
#Dataset({
#    features: ['image', 'label'],
#    num_rows: 27
#})
'''
#'''
dataset_dict = load_dataset("imagefolder", data_dir="download/image_classification/multiple_classes/grayscale/imagefolder")
#print(dataset_dict)
#DatasetDict({
#    train: Dataset({
#        features: ['image', 'label'],
#        num_rows: 32
#    })
#    validation: Dataset({
#        features: ['image', 'label'],
#        num_rows: 8
#    })
#})

train_dataset = dataset_dict['train']
validation_dataset = dataset_dict['validation']

#print(train_dataset)
#Dataset({
#    features: ['image', 'label'],
#    num_rows: 27
#})
#'''

for example in train_dataset:
    print(example['image']) #165.1
    print(example['label']) #151.892
    break
</pre>
