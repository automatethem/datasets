# custom-datasets

Download from github
<pre>
git clone https://github.com/automatethem/custom-datasets
</pre>

Supported custom datasets

<pre>
custom-datasets/audio_classification/audiofolder
custom-datasets/audio_classification/json

custom-datasets/automatic_speech_recognition/en

custom-datasets/image_captioning/json

custom-datasets/image_classification/binary_classes/imagefolder
custom-datasets/image_classification/multiple_classes/color/imagefolder
custom-datasets/image_classification/multiple_classes/grayscale/imagefolder
custom-datasets/custom-datasets/image_classification/multiple_classes/grayscale/json
custom-datasets/image_classification/multiple_labels/json

custom-datasets/image_segmentation/semantic

custom-datasets/object_detection

custom-datasets/question_answering/en

custom-datasets/recommendation

custom-datasets/sequence/many_to_many/char
custom-datasets/sequence/many_to_many/word

custom-datasets/siamese_classification

custom-datasets/summarization/en

custom-datasets/super_resolution/x1
custom-datasets/super_resolution/x4

custom-datasets/tabular_classification/bank_loan
custom-datasets/tabular_classification/iris

custom-datasets/tabular_regression/father_son_height
custom-datasets/tabular_regression/hyundae_car_price

custom-datasets/text_classification/char/ko/json
custom-datasets/text_classification/word/en/json
custom-datasets/text_classification/word/en/text
custom-datasets/text_classification/word/ko/json
custom-datasets/text_classification/word/ko/text

custom-datasets/text_generation/en/json
custom-datasets/text_generation/ko/json
custom-datasets/text_generation/ko/text

custom-datasets/time_series

custom-datasets/token_classification/en

custom-datasets/translation/de_en
</pre>

Custom dataset examples for machine learning.

download from github
<pre>
!git clone https://github.com/automatethem/download
</pre>

install datasets package
<pre>
pip install datasets
</pre>

python example
<pre>
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
</pre>

other examples

<a href="https://github.com/automatethem/download/tree/main/tabular_regression/father_son_height">tabular_regression/father_son_height</a><br>
<a href="https://github.com/automatethem/download/tree/main/image_classification/multiple_classes/grayscale">image_classification/multiple_classes/grayscale</a>


