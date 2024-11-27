import csv


class PathIterator:
    def __init__(self, path: str) -> None:
        self.path = path
        self.paths_list = self.__load_paths()
        self.limit = len(self.paths_list)
        self.current = 0

    def __iter__(self) -> 'PathIterator':
        return self


    def __next__(self) -> str:
        if self.current < self.limit:
            next_element = self.paths_list[self.current]
            self.current += 1
            return next_element
        else:
            raise StopIteration


    def __load_paths(self) -> list[str]:
        with open(self.path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            paths_list = [row[0] for row in reader]
        return paths_list