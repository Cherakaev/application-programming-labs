from HistTools import *
from ImageTools import *


"""


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
    print(image_size(image_1))
    image_2 = read_image('image.jpg')

    image_1 = cv2.resize(image_1, (400, 500))
    image_2 = cv2.resize(image_2, (500, 700))

    img_1_res, img_2_res = resize_to_single(image_1, image_2)

    image_h = image_hconcat(img_1_res, img_2_res)
    print_differences(image_1, image_h)

    save_image('file.jpg', image_h)

if __name__ == "__main__":
    main()