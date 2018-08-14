from typing import List, Tuple

__all__ = ["Page", "parse"]


class PageChoice:
    def __init__(self, text: str, pageID: str):
        self.text = text
        self.pageID = pageID


class Page:
    def __init__(
        self,
        name: str,
        text: List[str],
        choices: List[PageChoice]
    ):
        self.name = name
        self.text = text
        self.choices = choices


def parse(filepath: str) -> List[Page]:
    with open(filepath) as file:
        lines = file.readlines()

        # Remove comments
        for i in range(len(lines)):

if __name__ == "__main__":
    filename = ".\\CYOAFormat"
    # filename = input("Enter a filename> ")
    story = parse(filename)
