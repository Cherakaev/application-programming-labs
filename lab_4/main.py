import cv2
import pandas as pd


def make_data_frame(path_csv: str) -> pd.DataFrame:
    """
    Function makes DataFrame by using file.csv
    :param path_csv: string path to file.csv
    :return: DataFrame
    """
    data_frame = pd.read_csv(path_csv)
    data_frame.columns = (["abs_path", "rel_path"])
    return data_frame


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


def get_statistic(data_frame :pd.DataFrame):
    """

    :param data_frame: DataFrame with columns "Height", "Width", "Depth"
    :return:
    """
    stats = data_frame[["Height", "Width", "Depth"]].describe()
    return stats


def main():
    try:
        df = make_data_frame("../lab_2/annotation.csv")
        add_columns(df)
        stats = get_statistic(df)
        print(stats)
    except Exception as exc:
        print(f"Error: {exc}")

if __name__ == "__main__":
    main()