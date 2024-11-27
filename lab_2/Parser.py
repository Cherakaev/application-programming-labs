import argparse


def get_arguments() -> argparse.Namespace:
    """
    Function gets parameters from cmd
    :return: argparse.Namespace - simple argparse class which have parameters from cmd
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('key_word', type=str, help='print key word')
    parser.add_argument('dir_path', type=str, help='print directory path to save images')
    parser.add_argument('annotation_csv', type=str, help='print path to file.csv')
    args = parser.parse_args()
    return args