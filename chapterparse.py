"""

"""
import re


filename = "Charles Dickens.txt"


def chapter_parser():
    """ Chooses how to parse the file on chapters.
    """

    with open(filename, 'r') as f:
        contents = f.read()

    pattern = 'chapter.....'
    matches = re.findall(pattern, contents)

    print matches


def chapter_splitter():
    """
    """
    pass




if __name__ == '__main__':

    chapter_parser()





