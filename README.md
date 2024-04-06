# Football Detection Model
The model's goal is to detect players and ball on the pitch based on https://huggingface.co/datasets/keremberke/football-object-detection dataset. This repository contains two additional .py files: convert_to_gray.py, which converts images to gray using cv and download_data.py which is responsible for successfully downloading the data. Git and Python required to be installed and set up.

## Installation

### 1. Create & go to football_detection folder:
```bash
mkdir football_detection_v8 && cd football_detection_v8
```
### 2. Download all the files in this repository and paste them into 'football_detection' folder.
### 3. Install requirements
```bash
pip install -r requirements.txt
```
From now on you can use ultralytics directly with CLI with 'yolo' command.
### 4. Create a file called 'football-detection.yaml'
```bash
nano football-detection-v8.yaml
```
and paste inside:
```python
path: /home/pglowacki/piotr.glowacki2/football_detection_v8/data  # dataset root dir
train: train/images
val: val/images
test: test/images

# Classes
nc: 2  # number of classes
names:
  0: ball
  1: player
```
Be sure to adjust the absolute path to your needs.
### 5. Create a 'data' folder:
```bash
mkdir data
```
### 6. Install 'unzip' command if not already installed:
```bash
sudo apt install unzip
```

## Usage

### 1. Download the data
Go to 'data' folder:
```bash
cd data
```
* train set:
```bash
curl -L -o train.zip https://huggingface.co/datasets/keremberke/football-object-detection/resolve/main/data/train.zip
unzip train.zip -d train
rm train.zip
```
* test set:
```bash
curl -L -o test.zip https://huggingface.co/datasets/keremberke/football-object-detection/resolve/main/data/test.zip
unzip test.zip -d test
rm test.zip
```
* val set:
```bash
curl -L -o valid.zip https://huggingface.co/datasets/keremberke/football-object-detection/resolve/main/data/valid.zip
unzip valid.zip -d val
rm valid.zip
```
### 2. Convert to YOLO format
```bash
cd train
mkdir images labels
```
* move all the images (files with .jpg format) to 'images' folders:
```bash
mv *.jpg images/
```
* repeat it in test and val folders
```bash
cd ../test; mkdir images labels; mv *.jpg images/
cd ../val; mkdir images labels; mv *.jpg images/
```
* run the convert_to_yolo.py script in 'football_detection_v8' folder:
```bash
cd ..; python3 convert_to_yolo.py
```
### 3. Train the model
```bash
yolo train data=football-detection-v8.yaml model=yolov8m.pt epochs=50 lr0=0.01 imgsz=640 
```














### 3. Convert images to gray
```bash
python convert_images_to_gray.py
```

### 2. Clone yolov8 repository to the folder:
```bash
git clone https://github.com/ultralytics/ultralytics.git
```
### 3. Go to 'ultralytics' folder:
```bash
cd ultralytics
```
### 4. Download the weights from the repository (I used 'm' size of the model):
```bash
wget https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8m.pt
```
### 5. Go to 'ultralytics/cfg/models/v8' folder
```bash
cd ultralytics/cfg/models/v8
```
### 6. Copy 'yolov8.yaml' file:
```bash
cp yolov8.yaml football-detect.yaml
```
### 7. Change the number of classes in new file:
```bash
nano football-detect.yaml
```
```python
# parameters
nc: 2  # number of classes
```
### 8. Go to 'football_detection/ultralytics/ultralytics/data':
```bash
cd football_detection/ultralytics/ultralytics/data
```