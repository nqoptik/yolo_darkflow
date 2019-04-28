#!/usr/bin/env python3
import cv2
from darkflow.net.build import TFNet

# Define the model options and run
options = {
    "model": "cfg/tiny-yolo-voc-1c.cfg",
    "load": 6250,
    "threshold": 0.3,
    "gpu": 1.0
}
tfnet = TFNet(options)


for j in range(3300, 3615):
    # Read the color image
    formated_img_name = format(j, '06d') + ".jpg"
    img_file = "hourglass/hourglass_formated/" + formated_img_name
    img = cv2.imread(img_file, cv2.IMREAD_COLOR)

    # Use YOLO to predict the image
    result = tfnet.return_predict(img)

    # Pull out some info from the results
    for i in range(0, len(result)):
        tl = (result[i]["topleft"]["x"], result[i]["topleft"]["y"])
        br = (result[i]["bottomright"]["x"], result[i]["bottomright"]["y"])
        label = str(result[i]["confidence"])[:4]

        # Add the box and label
        img = cv2.rectangle(img, tl, br, (255, 0, 0), 2)
        img = cv2.putText(img, label, (tl[0], tl[1] + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

    # Show the image result
    cv2.imshow("img", img)
    if cv2.waitKey() & 0xFF == ord("q"):
        break
