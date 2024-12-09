from DataFrameTools import *
from HistTools import make_hist
from Parser import get_arguments


def main():
    try:
        args = get_arguments()
        df = make_data_frame(args.annotation_csv)
        print(df, "\n\n")

        add_columns(df)
        print(df, "\n\n")

        add_area(df)
        print(df, "\n\n")

        sorted_df_1 = sort_height_width(df, 1000, 900)
        print(sorted_df_1, "\n\n")

        sorted_df_2 = sort_area(df)
        print(sorted_df_2, "\n\n")

        stats = get_statistic(df)
        print(stats)

        make_hist(df)
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()