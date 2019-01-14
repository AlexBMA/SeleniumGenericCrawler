import cv2
import numpy as np


def has_Image():



    return ""


def main():

    original = cv2.imread("images_image_comparison/images/original_golden_bridge.jpg")
    duplicate = cv2.imread("images_image_comparison/images/duplicate.jpg")


    # 1) Check if 2 images are equals

    if original.shape == duplicate.shape:
        print("The images have the save height and channels")

    cv2.imshow("original", original)
    cv2.imshow("duplicate",duplicate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


main()