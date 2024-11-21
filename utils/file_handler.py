# For saving and loading files like images
import os

import cv2

def save_qr_image(image, path):
    image.save(path)
    print(f"QR code image saved at {path}")

def load_qr_image(path):
    if os.path.exists(path):
        return cv2.imread(path)
    else:
        raise FileNotFoundError("The provided QR code image does not exist.")
