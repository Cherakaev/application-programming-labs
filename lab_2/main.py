import argparse
import csv
import os
from icrawler.builtin import GoogleImageCrawler

def get_arguments() -> list:
    """
    function ret
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('key_word', type=str, help='print key word')
    parser.add_argument('directory_path', type=str, help='print directory path to save images')
    parser.add_argument('file_csv_path', type=str, help='print path of csv file')
    args = parser.parse_args()
    return [args.key_word, args.directory_path, args.file_csv_path]


def get_images(key_word: str, directory_path: str, max_num: int):
    """
    function downloads images from Google to the directory by using key word

    :param key_word: word to google images
    :param directory_path: directory to save images
    :param max_num: number of images to download
    :return: None
    """
    google_crawler = GoogleImageCrawler(storage={'root_dir': directory_path})
    google_crawler.crawl(keyword=key_word, max_num=max_num)


def main() -> None:
    try:
        list_of_arguments = get_arguments()
        get_images(list_of_arguments[0], list_of_arguments[1], 5)
        with open(list_of_arguments[2], mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["absolute_path", "relative_path"])

            for filename in os.listdir(list_of_arguments[1]):
                if filename.endswith(('jpg', 'jpeg', 'png')):
                    abs_path = os.path.abspath(os.path.join(list_of_arguments[1], filename))
                    rel_path = os.path.relpath(abs_path, list_of_arguments[1])
                    writer.writerow([abs_path, rel_path])

    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()