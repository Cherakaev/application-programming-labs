from HistTools import *
from ImageTools import *
from Parser import get_arguments


def main():
    try:
        args = get_arguments()

        image_1 = read_image(args.image_path)
        image_2 = read_image(args.image_path)

        image_2 = cv2.resize(image_1, (500, 500))

        img_1_res, img_2_res = resize_to_single(image_1, image_2)
        image_h = image_hconcat(img_1_res, img_2_res)

        print(image_size(image_1))
        show_image( image_1, 'original')
        show_image(image_h, 'result')

        save_image('file.jpg', image_h)

        hist = make_hist(image_1)
        show_hist(hist)
    except Exception as exc:
        print(f"Error: {exc}")

if __name__ == "__main__":
    main()