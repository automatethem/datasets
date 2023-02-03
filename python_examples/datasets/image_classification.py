#pip install datasets

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
    print(example['image']) #<PIL.PngImagePlugin.PngImageFile image mode=L size=28x28 at 0x7F3C2566AD60>
    print(example['label']) #0
    break
