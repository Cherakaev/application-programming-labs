import csv
import os


def weed_out_images(dir_path: str) -> list[str]:
    """
    Function goes through folder and adds all paths
    file types .png .jpg. jpeg to list

    :param dir_path: directory to your folder with images
    :return: list of paths of images
    """
    if os.path.isdir(dir_path):
        list_of_paths = []
        for filename in os.listdir(dir_path):
            if filename.endswith(('png', 'jpg', 'jpeg')):
                list_of_paths.append(filename)
        return list_of_paths
    else:
        list_of_paths = []
        for filename in os.listdir("new_images"):
            if filename.endswith(('png', 'jpg', 'jpeg')):
                list_of_paths.append(filename)
        return list_of_paths


def create_annot(annotation_path: str, list_of_paths: list[str]) -> None:
    """
    Function makes annotation of paths in file.csv

    :param annotation_path: path to your file.csv
    :param list_of_paths: list of paths which will be used to make annotation
    :return: None
    """
    with open(annotation_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Absolute_path", "Relative_path"])
        for path in list_of_paths:
                abs_path = os.path.abspath(path)
                rel_path = os.path.relpath(path, os.curdir)
                writer.writerow([abs_path, rel_path])