import argparse


def get_arguments() -> argparse.Namespace:
    """
    Function ret
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('image_path', type=str, help='print path to your image')
    args = parser.parse_args()
    return args