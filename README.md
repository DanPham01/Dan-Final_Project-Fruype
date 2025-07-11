
# Fruype

An AI system measures the fruit's ripeness and send back the data to the user, which can be used from small gardens to large farms management.

## Overview

This AI uses model yolov8 as a base and learns from a variety of large dataset to precisely distinguish between each phase of ripeness of a fruit with the percentage of confidence. There are two main way to operate, either by talking a picture manually to dectect or detect live through fixed camera. Fruype has various impacts:

To farms:
- Efficiency: Help farmers manage their plants easier anywhere and anytime
- Friendly: Easy to use, easy to access, help unprofessionals practice some farming
- Developable: The model is open for further personalize training and developing
To developers: 
- Collect diverse data from user for AI training and improve speed and accuracy

1. Create a directory of the project

2. Download  Jetson-Inference by cloning from GitHub inside the directory
- git clone --recursive https://github.com/dusty-nv/jetson-inference
- cd jetson-inference
- mkdir build
- cd build

3. CMake is a C++ build tool that configures projects for your Jetpack version
- cmake ../
- You will see this PyTorch installer
    - //image//
    - Press space to select and then enter to install
- make -j$(nproc)
- sudo make install
- sudo ldconfig

4. Install the dataset
- Here I use "Fruit-Ripeness-Dataset" on Kaggle: https://www.kaggle.com/datasets/asadullahprl/fruits-ripeness-classification-dataset/data
- Download dataset as zip into your file explorer and then unzip into
- Import the files inside the most outside file into your data folder in VSCode

5. Train the model

- pip install ultralytics
    //Download the yolov8 model//
- pip uninstall  numpy
- pip install numpy==1.23.0
- yolo task=classify mode=train model=yolov8n-cls.pt data=/home/nvidia08/Dan-Final_Project-Fruype/dataset epochs=50 imgsz=224

?. Run the model
- yolo task=classify mode=val model=runs/classify/train3/weights/best.pt data=/home/nvidia08/Dan-Final_Project-Fruype/dataset
- yolo task=classify mode=predict model=runs/classify/train3/weights/best.pt source=/home/nvidia08/Dan-Final_Project-Fruype/classification //Detect images//
- yolo task=classify mode=predict model=runs/classify/train3/weights/best.pt source=0 //Detect live through webcam//

Note: You would like to use the model code that you have for "model=" and input data (after trained) for "source=" 



