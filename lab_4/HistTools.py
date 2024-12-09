import matplotlib.pyplot as plt
import pandas as pd


def make_hist(data_frame :pd.DataFrame) -> None:
    """
    Function makes histogram by using DataFrame
    :param data_frame:  DataFrame with column "Area"
    :return: None
    """
    plt.figure(figsize=(10, 7))
    plt.hist(data_frame["Area"], bins=100, edgecolor='black')
    plt.title("Histogram of DataFrame")
    plt.xlabel("Areas size")
    plt.ylabel("Amount of areas")

    plt.show()