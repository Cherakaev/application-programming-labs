import argparse


def get_arguments() -> argparse.Namespace:
    """
    Function gets parameters from cmd
    :return: argparse.Namespace - simple argparse class which have parameters from cmd
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('annotation_csv', type=str, help='print path to file.csv')
    args = parser.parse_args()
    return args