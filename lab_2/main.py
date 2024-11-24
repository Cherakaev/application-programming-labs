from Get_images import get_images
from Make_annotation import weed_out_images
from Make_annotation import create_annot
from Parser import get_arguments
from PathIterator import PathIterator


def main() -> None:
    try:
        args = get_arguments()
        get_images(args.key_word, args.dir_path, 50)
        list_of_paths = weed_out_images(args.dir_path)
        create_annot(args.annotation_csv, list_of_paths)
        iterator = PathIterator(args.annotation_csv)
        for i in iterator:
            print(i)

    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()