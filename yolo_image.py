#!/usr/bin/env python3
import cv2
from darkflow.net.build import TFNet

# Define the model options and run
options = {
    "model": "cfg/yolo.cfg",
    "load": "bin/yolov2.weights",
    "threshold": 0.3,
    "gpu": 1.0
}
tfnet = TFNet(options)

# Read the color image
img_file = "dog.jpg"
img = cv2.imread(img_file, cv2.IMREAD_COLOR)

# Use YOLO to predict the image
result = tfnet.return_predict(img)

# Pull out some info from the results
for i in range(0, len(result)):
    tl = (result[i]["topleft"]["x"], result[i]["topleft"]["y"])
    br = (result[i]["bottomright"]["x"], result[i]["bottomright"]["y"])
    label = result[i]["label"]

    # Add the box and label
    img = cv2.rectangle(img, tl, br, (255, 0, 0), 2)
    img = cv2.putText(img, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

# Show the image result
cv2.imshow("img", img)
cv2.waitKey()
