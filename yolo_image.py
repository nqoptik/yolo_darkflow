#!/usr/bin/env python3
import cv2
from darkflow.net.build import TFNet

# Define the model options and run
options = {
    "model": "cfg/tiny-yolo-voc-2c.cfg",
    "load": 4250,
    "threshold": 0.3,
    "gpu": 0.8
}
tfnet = TFNet(options)


for j in range(1000, 1200):
    # Read the color image
    formated_img_name = format(j, '06d') + ".jpg"
    img_file = "giant_images/" + formated_img_name
    img = cv2.imread(img_file, cv2.IMREAD_COLOR)

    # Use YOLO to predict the image
    results = tfnet.return_predict(img)

    # Pull out some info from the results
    for result in results:
        tl = (result["topleft"]["x"], result["topleft"]["y"])
        br = (result["bottomright"]["x"], result["bottomright"]["y"])
        confidence = str(result["confidence"])[:4]
        label = result["label"]

        # Add the box and confidence
        img = cv2.rectangle(img, tl, br, (255, 0, 0), 2)
        if label == "giant_location":
            img = cv2.putText(img, confidence, (tl[0], tl[1] + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        elif label == "qr_tag":
            img = cv2.putText(img, confidence, (tl[0], tl[1] + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    # Show the image results
    cv2.imshow("img", img)
    if cv2.waitKey() & 0xFF == ord("q"):
        break
