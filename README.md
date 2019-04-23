# YOLO darkflow
A simple repository to try out YOLO v2

# Prerequisites
## tensorflow-gpu
You can follow this [install tensorflow-gpu](https://github.com/Nguyen-Quang/instructions/blob/master/install_tensorflow_gpu.md) instruction to install tensorflow-gpu.

## Cython
Install Cython by typing:
```
pip3 install Cython
pip install Cython
```

## openCV
You can follow this [install opencv3 cuda](https://github.com/Nguyen-Quang/instructions/blob/master/install_opencv3_cuda.md) instruction to install openCV.

## darkflow
Clone darkflow repository from github:
```
git clone https://github.com/thtrieu/darkflow
```

Let's install darkflow globally:
```
cd darkflow
pip3 install .
pip install .
```

To uninstall darkflow, simply run this command:
```
pip3 uninstall darkflow
pip uninstall darkflow
```

# Installing
Clone the repository from github:
```
git clone https://github.com/Nguyen-Quang/yolo_darkflow.git
```

# Running the tests

Download weights file from https://pjreddie.com/media/files/yolov2.weights and place it to `bin/`. There are other weights file on https://pjreddie.com/darknet/yolo/ that you can try.

Let's take a sample video called video.mkv, and process it:
```
cd yolo_darkflow
python3 flow --model cfg/yolo.cfg --load bin/yolov2.weights --demo video.mkv --gpu 1.0 --saveVideo
```
