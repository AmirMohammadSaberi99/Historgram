# color_histogram.py

import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt

def plot_color_histogram(image_path):
    # Load the image in BGR
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Cannot load image: {image_path}")

    # Split into B, G, R channels
    chans = cv2.split(img)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

    # compute histogram for each channel
    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist(
            [chan],             # source image(s)
            [0],                # channel index (here only one channel)
            None,               # mask (None = full image)
            [256],              # histogram size (bins)
            [0, 256]            # range of pixel values
        )
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

    plt.legend(("Blue", "Green", "Red"))
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compute and plot per-channel histogram with cv2.calcHist()"
    )
    parser.add_argument("image", help="Path to the input color image")
    args = parser.parse_args()

    plot_color_histogram(args.image)
