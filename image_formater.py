#!/usr/bin/env python3
import cv2
import os
from os import listdir
from os.path import isfile, join


# Define resolution thresholds
RESOLUTION_LEVEL_0 = 2000000
RESOLUTION_LEVEL_1 = 9000000


def get_filename_list_by_resolution(directory):
    """Get filename list with increasing resolution"""

    # List of files in the directory
    filename_list = [f for f in listdir(directory) if isfile(join(directory, f))]

    # Loop and add files with resolutions to the list
    filename_with_resolution_list = []
    for filename in filename_list:
        gg_file_path = os.path.join(directory, filename)
        print("Read: " + gg_file_path)
        img = cv2.imread(gg_file_path)

        # Resolution = 0 if the file isn't not an image
        formated_resolution = 0
        if str(img) == "None":
            pass

        # Calculate images' resolutions
        else:
            width, height = img.shape[:2]
            resolution = width * height

            # Keep the image the same if its resolution is less than RESOLUTION_LEVEL_0
            if resolution < RESOLUTION_LEVEL_0:
                formated_resolution = resolution

            # Resize image with scale factor = 0.5 if its resolution is greater or equal to RESOLUTION_LEVEL_0 and less than RESOLUTION_LEVEL_1
            elif resolution < RESOLUTION_LEVEL_1:
                formated_resolution = resolution/4

            # Resize image with scale factor = 0.25 if its resolution is greater or equal to RESOLUTION_LEVEL_1
            else:
                formated_resolution = resolution/16

        filename_with_resolution_list.append((filename, formated_resolution))

    # Sort list by the first element, resolution.
    filename_with_resolution_list.sort(key=lambda r: r[1])

    # Get the filename list
    filename_list = []
    for filename_with_resolution in filename_with_resolution_list:
        filename_list.append(filename_with_resolution[0])

    return filename_list


def format_and_rename_images(src_directory, dst_directory, filename_list):
    """Format, rename and save images"""

    img_num = 0
    for filename in filename_list:
        gg_file_path = os.path.join(src_directory, filename)
        print("Process: " + gg_file_path)
        img = cv2.imread(gg_file_path)

        # Delete the file if it's not an image
        if str(img) == "None":
            rm_str = "rm" + " " + gg_file_path
            os.system(rm_str)

        # Rename image and save to the formated directory
        else:
            width, height = img.shape[:2]
            resolution = width * height

            # Keep the image the same if its resolution is less than RESOLUTION_LEVEL_0
            if resolution < RESOLUTION_LEVEL_0:
                pass

            # Resize image with scale factor = 0.5 if its resolution is greater or equal to RESOLUTION_LEVEL_0 and less than RESOLUTION_LEVEL_1
            elif resolution < RESOLUTION_LEVEL_1:
                img = cv2.resize(img, None, fx=0.5, fy=0.5)

            # Resize image with scale factor = 0.25 if its resolution is greater or equal to RESOLUTION_LEVEL_1
            else:
                img = cv2.resize(img, None, fx=0.25, fy=0.25)

            # Rename and save images
            formated_img_name = format(img_num, '06d') + ".jpg"
            formated_img_path = os.path.join(dst_directory, formated_img_name)
            cv2.imwrite(formated_img_path, img)
            img_num += 1

            # Delete the file
            rm_str = "rm" + " " + gg_file_path
            os.system(rm_str)


def main():
    """The main function"""

    # Working directories
    google_dir = "hourglass/hourglass_google"
    formated_dir = "hourglass/hourglass_formated"
    os.system("mkdir" + " " + formated_dir)

    # Get filename list with increasing resolution
    filename_list = get_filename_list_by_resolution(google_dir)

    # Format, rename and save images
    format_and_rename_images(google_dir, formated_dir, filename_list)


if __name__ == "__main__":
    main()
