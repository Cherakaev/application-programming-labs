import cv2
import matplotlib.pyplot as plt
import numpy as np


def make_hist(image: np.ndarray) -> tuple:
    """
    Function makes histogram of image
    :param image: original image
    :return: tuple with histograms
    """
    hist_b = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([image], [1], None, [256], [0, 256])
    hist_r = cv2.calcHist([image], [2], None, [256], [0, 256])
    return hist_b, hist_g, hist_r

def show_hist(hist: tuple) -> None:
    """
     Function builds graphics and shows histogram
     :param hist: tuple with histograms for blue, green and red colours
     :return: None
     """
    plt.figure(figsize=(10, 6))
    plt.title("Histogram of image")
    plt.xlabel("Values of pixels")
    plt.ylabel("Frequency of colour")

    plt.plot(hist[0], color='blue', label='Blue channel')
    plt.plot(hist[1], color='green', label='Green channel')
    plt.plot(hist[2], color='red', label='Red channel')

    plt.xlim([0, 256])
    plt.legend()
    plt.show()