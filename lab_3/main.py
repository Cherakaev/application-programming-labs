import cv2
import numpy as np
import matplotlib.pyplot as plt

import ImageTools
from ImageTools import read_image, image_size, image_hconcat, show_image, reduce_to_single

"""img = cv2.imread('image.jpg')
img2 = cv2.imread('image.jpg')

image1_resized = cv2.resize(img, (500, 500))  # Задайте нужный размер
image2_resized = cv2.resize(img2, (500, 500))

im_h = cv2.hconcat([image1_resized, image2_resized])
cv2.imshow('himage.jpeg', im_h)

print("Image size is ", img.shape)


plt.figure(figsize=(10, 6))
histb = cv2.calcHist(img, [0], None, [256], [0, 256])
histr = cv2.calcHist(img, [1], None, [256], [0, 256])
histg = cv2.calcHist(img, [2], None, [256], [0, 256])
plt.title('Image Histogram Channel GFG')

plt.plot(histb, color = 'blue', label = 'Blue channel')
plt.plot(histg, color = 'green', label = 'Green channel')
plt.plot(histr, color = 'red', label = 'Red channel')

plt.xlim([0, 256])
plt.legend()
plt.grid(True)
plt.show()"""

def main():
    image_1 = read_image('image.jpg')
    image_2 = read_image('image.jpg')

    image_1 = cv2.resize(image_1, (400, 500))
    image_2 = cv2.resize(image_2, (500, 700))

    list_of_img = [image_1, image_2]
    list_of_img = reduce_to_single(list_of_img)

    print(image_size(list_of_img[0]))
    print(image_size(list_of_img[1]))

    image_h = image_hconcat(list_of_img)
    print(image_size(image_h))
    show_image(image_h)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()