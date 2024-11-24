from icrawler.builtin import GoogleImageCrawler
from os import path, mkdir


def get_images(key_word: str, dir_path: str, max_num: int) -> None:
    """
    Function downloads images from Google to the folder by using key word

    :param key_word: word to google images
    :param dir_path: path to directory to save images
    :param max_num: number of images to download
    :return: None
    """

    if path.isdir(dir_path):
        google_crawler = GoogleImageCrawler(storage={'root_dir': dir_path})
        google_crawler.crawl(keyword=key_word, max_num=max_num)
    else:
        mkdir("new_images")
        google_crawler = GoogleImageCrawler(storage={'root_dir': "new_images"})
        google_crawler.crawl(keyword=key_word, max_num=max_num)