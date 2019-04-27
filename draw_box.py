#!/usr/bin/env python3
import os
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector
from generate_xml import write_xml


# Global variables
img = None
tl_list = []
br_list = []
object_list = []


# Constants
IMAGE_FOLDER = "hourglass/hourglass_formated"
SAVE_DIR = "annotations"
OBJECT = "hourglass"


def line_select_callback(clk, rls):
    global tl_list
    global br_list
    global object_list
    tl_list.append((int(clk.xdata), int(clk.ydata)))
    br_list.append((int(rls.xdata), int(rls.ydata)))
    object_list.append(OBJECT)


def onkeypress(event):
    global object_list
    global tl_list
    global br_list
    global img
    if event.key == "q":
        print(object_list)
        write_xml(IMAGE_FOLDER, img, object_list, tl_list, br_list, SAVE_DIR)
        tl_list = []
        br_list = []
        object_list = []
        img = None
        plt.close()


def toggle_selector(event):
    toggle_selector.RS.set_active(True)


def sort_file_by_path_name(folder):
    """Sort image file by path name"""

    file_with_path_list = []
    for file in os.scandir(folder):
        file_with_path_list.append((file, file.path))
    file_with_path_list.sort(key=lambda r: r[1])
    file_sorted_list = []
    for file_with_path in file_with_path_list:
        file_sorted_list.append(file_with_path[0])
    return file_sorted_list


if __name__ == "__main__":
    """The main function"""

    # Sort image file by path name
    image_file_sorted_list = sort_file_by_path_name(IMAGE_FOLDER)
    for image_file in image_file_sorted_list[:100]:
        print(image_file.path)
        img = image_file
        fig, ax = plt.subplots(1)
        image = cv2.imread(image_file.path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ax.imshow(image)

        toggle_selector.RS = RectangleSelector(
            ax, line_select_callback,
            drawtype="box", useblit=True,
            button=[1], minspanx=3, minspany=3,
            spancoords="pixels", interactive=True
        )
        bbox = plt.connect("key_press_event", toggle_selector)
        key = plt.connect("key_press_event", onkeypress)
        plt.show()
