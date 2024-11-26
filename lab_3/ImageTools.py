import cv2
import numpy as np


def read_image(path_image: str) -> np.ndarray:
    """
    Function reads image from file
    :param: path_image: path to image
    :return: image as an array
    """
    image = cv2.imread(path_image)
    return image


def image_size(image: np.ndarray) -> tuple:
    """
    Function gets height and width of the image
    :param image: image as an array
    :return: tuple with 2 parameters
    """
    img_tuple = (image.shape[0], image.shape[1])
    return img_tuple


def image_hconcat(image_1:np.ndarray, image_2:np.ndarray) -> np.ndarray:
    """
    Functions concatenate 2 images into 1 horizontal
    :param image_1: readed image as an array
    :param image_2: image as an array
    :return: new bigger image as an array
    """
    image_h = cv2.hconcat([image_1, image_2])
    return image_h


def image_vconcat(image_1:np.ndarray, image_2:np.ndarray) -> np.ndarray:
    """
    Functions concatenate 2 images into 1 vertical
    :param image_1: image as an array
    :param image_2: image as an array
    :return: new bigger image as an array
    """
    image_v = cv2.vconcat([image_1, image_2])
    return image_v


def show_image(image:np.ndarray, name:str) -> None:
    """
    Function shows image
    :param image: image as an array
    :return: None
    """
    cv2.imshow(name, image)
    cv2.waitKey(0)


def resize_to_single(image_1:np.ndarray, image_2:np.ndarray) -> tuple:
    """
    Function makes 2 new resized images by using shapes of original images
    :param image_1: image as an array
    :param image_2: image as an array
    :return: tuple of 2 new resized images
    """
    height1, width1 = image_1.shape[:2]
    height2, width2 = image_2.shape[:2]

    min_height = min(height1, height2)
    min_width = min(width1, width2)

    image_1_resized = cv2.resize(image_1, (min_width, min_height))
    image_2_resized = cv2.resize(image_2, (min_width, min_height))

    return image_1_resized, image_2_resized


def save_image(file_path: str, image: np.ndarray) -> None:
    """
    Function saves image to file
    :param file_path: path to file
    :param image: saving image
    :return: None
    """
    try:

        cv2.imwrite(file_path, image)
    except:
        raise Exception('Could not save image')