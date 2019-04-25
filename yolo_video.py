#!/usr/bin/env python3
import cv2
from darkflow.net.build import TFNet

import numpy as np
import time

# Define the model options and run
options = {
    "model": "cfg/yolo.cfg",
    "load": "bin/yolov2.weights",
    "threshold": 0.3,
    "gpu": 1.0
}
tfnet = TFNet(options)

# Random colors tuple
corlors = [tuple(255*np.random.rand(3)) for _ in range(20)]

# Video capture
capture = cv2.VideoCapture("video.mkv")
while (capture.isOpened()):
    stime = time.time()

    # Capture new frame
    ret, frame = capture.read()
    if ret:
        # Use YOLO to predict the image
        results = tfnet.return_predict(frame)
        for color, result in zip(corlors, results):
            # Get the results
            tl = (result["topleft"]["x"], result["topleft"]["y"])
            br = (result["bottomright"]["x"], result["bottomright"]["y"])
            label = result["label"]

            # Add the box and label
            cv2.rectangle(frame, tl, br, color, 2)
            cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

        # Display the frame
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        # Print out the FPS
        print("FPS {:.1f}".format(1 / (time.time() - stime)))

    else:
        capture.release()
        cv2.destroyAllWindows()
        break
