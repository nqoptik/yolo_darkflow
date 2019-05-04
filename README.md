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

## Process video
Let's take a sample video called video.mkv, and process it:
```
cd yolo_darkflow
python3 flow --model cfg/yolo.cfg --load bin/yolov2.weights --demo video.mkv --gpu 0.8 --saveVideo
```

or:
```
python3 yolo_video.py
```

## Train on our own dataset
The steps below assume we want to use tiny YOLO and our dataset has 2 classes

### Step 1.
Create a copy of the configuration file `tiny-yolo-voc.cfg` and rename it according to your preference `tiny-yolo-voc-2c.cfg`.

It is crucial that you leave the original `tiny-yolo-voc.cfg` file unchanged. When darkflow sees you are loading `tiny-yolo-voc.weights` it will look for `tiny-yolo-voc.cfg` in your cfg/ folder and compare that configuration file to the new one you have set with `--model cfg/tiny-yolo-voc-2c.cfg`. In this case, every layer will have the same exact number of weights except for the last two, so it will load the weights into all layers up to the last two because they now contain a different number of weights.

### Step 2.
In `tiny-yolo-voc-2c.cfg`, change classes in the [region] layer (the last layer) to the number of classes you are going to train for. In our case, classes are set to 2.
    
```
...
[region]
anchors = 1.08,1.19,  3.42,4.41,  6.63,11.38,  9.42,5.11,  16.62,10.52
bias_match=1
classes=2
coords=4
num=5
softmax=1
...
```

### Step 3.
In `tiny-yolo-voc-2c.cfg`, change filters in the [convolutional] layer (the second to last layer) to num * (classes + 5). In our case, num is 5 and classes is 2 so 5 * (2 + 5) = 35 therefore filters are set to 35.

```
...
[convolutional]
size=1
stride=1
pad=1
filters=35
activation=linear
...
```

### Step 4.
Change `labels.txt` to include the label(s) you want to train on (number of labels should be the same as the number of classes you set in `tiny-yolo-voc-2c.cfg` file). In our case, `labels.txt` will contain 2 labels.

```
giant_location
qr_tag
```
### Step 5.
Reference the `tiny-yolo-voc-2c.cfg` model when you train.
```
python3 flow --model cfg/tiny-yolo-voc-2c.cfg --load bin/tiny-yolo-voc.weights --train --annotation giant_annotations --dataset giant_images --gpu 0.8 --epoch 500
```

## Test the results
Change the model option in `yolo_image.py` to:
```
options = {
    "model": "cfg/tiny-yolo-voc-2c.cfg",
    "load": 4250,
    "threshold": 0.3,
    "gpu": 0.8
}
tfnet = TFNet(options)
```
in which, `4250` is one of the checkpoint loop inside `ckpq` folder.

Let's rung the detection:
```
python3 yolo_image.py
```
