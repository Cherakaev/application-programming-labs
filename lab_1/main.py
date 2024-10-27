import argparse
import re


def get_filepath() -> str:

    #function gets file path from cmd
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str, help='your filepath')
    args = parser.parse_args()
    return args.filepath


def read_file(file_path: str) -> str:
    #function reads file into string using file path
    with open(file_path, 'r', encoding='utf-8') as file:
        text: str = file.read()
        return text


def split_forms(text: str) -> list[str]:
    #function splits string into list_of_strings
    pattern = r'\d+[)]'
    text = text.strip()
    list_of_forms: list[str] = re.split(pattern, text)
    return list_of_forms


def find_moscow(list_of_forms: list[str]) -> list[str]:
    #function return list of forms with Москва in it
    new_list_of_forms = []
    for form in list_of_forms:
        if 'Москва' in form:
            new_list_of_forms.append(form)
    return new_list_of_forms


def print_forms(list_of_forms: list[str]):
    #function prints all forms
    for form in list_of_forms:
        print(form.strip(), '\n')


def main() -> None:
    try:
        filepath = get_filepath()
        text = read_file(filepath)
        list_of_forms = split_forms(text)
        list_of_forms = find_moscow(list_of_forms)
        print_forms(list_of_forms)
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
