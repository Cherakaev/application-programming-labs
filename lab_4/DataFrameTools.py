import cv2
import pandas as pd


def make_data_frame(path_csv: str) -> pd.DataFrame:
    """
    Function makes DataFrame by using file.csv
    :param path_csv: string path to file.csv
    :return: DataFrame
    """
    try:
        data_frame = pd.read_csv(path_csv)
        data_frame.columns = (["abs_path", "rel_path"])
        return data_frame
    except:
        raise Exception("Couldn't read the annotation")


def  add_columns(data_frame :pd.DataFrame) -> None:
    """
    Function adds 3 columns to DataFrame: Height, Width, Depth
    :param data_frame: DataFrame with column "abs_path"
    :return: None
    """
    images = [cv2.imread(img) for img in data_frame["abs_path"]]
    data_frame["Height"] = [img.shape[0] for img in images]
    data_frame["Width"] = [img.shape[1] for img in images]
    data_frame["Depth"] = [img.shape[2] for img in images]


def get_statistic(data_frame :pd.DataFrame) -> pd.DataFrame:
    """
    Function returns new DataFrame with statistic information about data_frame
    :param data_frame: DataFrame with columns "Height", "Width", "Depth"
    :return: DataFrame with statistic information about data_frame
    """
    return data_frame[["Height", "Width", "Depth"]].describe()


def sort_height_width(data_frame :pd.DataFrame, max_height: int, max_width: int) -> pd.DataFrame:
    """
    Function sorts images in DataFrame by using max_height and max_width
    :param data_frame: DataFrame with columns "Height", "Width"
    :param max_height: int number if pixels
    :param max_width:  int number if pixels
    :return: sorted DataFrame
    """
    sorted_df = data_frame[(data_frame["Height"] < max_height) & (data_frame["Width"] < max_width)]
    return sorted_df


def add_area(data_frame :pd.DataFrame) -> None:
    """
    Function adds new column "Area" that equals Height * Width
    :param data_frame: DataFrame with columns "Height", "Width"
    :return: None
    """
    data_frame["Area"] = data_frame["Height"]*data_frame["Width"]


def sort_area(data_frame :pd.DataFrame) -> pd.DataFrame:
    """
    Function sorts DataFrame by area from lowest to biggest
    :param data_frame: DataFrame with columns "Area"
    :return: sorted DataFrame
    """
    sorted_df = data_frame.sort_values(by = "Area",  ascending=True,   inplace=False)
    return sorted_df