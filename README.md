# Football Detection Model
This repository is designed to detect football players and the ball on the pitch using the [football-object-detection dataset](https://huggingface.co/datasets/keremberke/football-object-detection) hosted on Hugging Face. It includes utility script for converting annotations to YOLO format, as in original dataset the annotations files format is COCO.

## Prerequisites
Ensure you have Git and Python installed on your system. Additionally, `unzip` utility should be installed to handle data extraction:
```bash
sudo apt install git python3 python3-pip unzip
```
## Setup
#### 1. Create and navigate to the project directory:
```bash
mkdir football_detection_v8 && cd football_detection_v8
```
#### 2. Clone this repository:
```bash
git clone https://github.com/piotr-glowacki/football-detection-yolov8.git
```
#### 3. Install dependencies:
```bash
pip install -r requirements.txt
```
#### 4. Adjust the path in dataset configuration as necessary:
```bash
nano football-detection-v8.yaml
```
#### 5. Prepare the data directory:
```bash
mkdir data
```

## Usage
### Data Management
#### 1. Navigate to the data directory:
```bash
cd data
```
#### 2. Download and extract the datasets:
* For the training set:
```bash
curl -L -o train.zip https://huggingface.co/datasets/keremberke/football-object-detection/resolve/main/data/train.zip
unzip train.zip -d train
rm train.zip
```
* For the test set:
```bash
curl -L -o test.zip https://huggingface.co/datasets/keremberke/football-object-detection/resolve/main/data/test.zip
unzip test.zip -d test
rm test.zip
```
* For the val set:
```bash
curl -L -o valid.zip https://huggingface.co/datasets/keremberke/football-object-detection/resolve/main/data/valid.zip
unzip valid.zip -d val
rm valid.zip
```
### Preprocessing
#### 1. Organize images and labels in appropriate directories:
```bash
cd train && mkdir images labels && mv *.jpg images/
cd ../test && mkdir images labels && mv *.jpg images/
cd ../val && mkdir images labels && mv *.jpg images/
cd ..
```
#### 2. Convert dataset to YOLO format:
```bash
python3 convert_to_yolo.py
```
#### 3. Train the model
```bash
yolo train data=football-detection-v8.yaml model=yolov8m.pt epochs=50 imgsz=640 
```
