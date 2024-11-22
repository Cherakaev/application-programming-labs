import argparse
import csv
import os
from icrawler.builtin import GoogleImageCrawler


class ImageIterator:
    def __init__(self, annotation: str):
        with open (annotation, 'r') as file:
            reader = csv.reader(file)
            self.images = [i for i in reader]
        self.limit = len(self.images)
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            result = self.images[self.current]
            self.current += 1
            return result
        else:
            raise StopIteration

    def to_start(self):
        self.current = 0


def get_arguments() -> argparse.Namespace:
    """
    function ret
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('key_word', type=str, help='print key word')
    parser.add_argument('folder', type=str, help='print folder path to save images')
    parser.add_argument('annotation_csv', type=str, help='print path of csv file')
    args = parser.parse_args()
    return args


def get_images(key_word: str, folder_path: str, max_num: int):
    """
    function downloads images from Google to the folder by using key word

    :param key_word: word to google images
    :param folder_path: folder to save images
    :param max_num: number of images to download
    :return: None
    """
    google_crawler = GoogleImageCrawler(storage={'root_dir': folder_path})
    google_crawler.crawl(keyword=key_word, max_num=max_num)


def main() -> None:
    try:
        args = get_arguments()
        get_images(args.key_word, args.folder, 5)
        with open(args.annotation_csv, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["absolute_path", "relative_path"])

            for filename in os.listdir(args.folder):
                if filename.endswith(('jpg', 'jpeg', 'png')):
                    abs_path = os.path.abspath(os.path.join(args.folder, filename))
                    rel_path = os.path.relpath(abs_path, args.folder)
                    writer.writerow([abs_path, rel_path])
        image_iterator = ImageIterator(args.annotation_csv)
        for i in image_iterator:
            print(i)

    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()