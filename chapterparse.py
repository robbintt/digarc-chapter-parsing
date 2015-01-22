"""

Steps:
We want to identify the formatting pattern from a preselected set.
Then we want to parse the text on that formatting pattern.

"""
import re

filename = "Charles Dickens.txt"

"""
A few different cases for chapter itself.
Case 1: Roman Numerals 'ivmcxl'
Case 2: Arabic Numbers 0-9
Case 3: A list of written numbers one to twenty, followed by thirty, forty, fifty, etc

The word 'chapter' will be case insensitive.

Next lets do a frequency search for each case in the document and identify the major case.
"""


arabic_pattern = "CHAPTER [0-9]" # All needs case insensitive.
roman_numeral_pattern = "CHAPTER [ivxlcm]" # all needs case insensitive

written_numbers = [
"one",
"two",
"three",
"four",
"five",
"six",
"seven",
"eight",
"nine",
"ten",
"eleven",
"twelve",
"thirteen",
"fourteen",
"fifteen",
"sixteen",
"seventeen",
"eighteen",
"nineteen",
"twenty",
"thirty",
"forty",
"fifty",
"sixty",
"seventy",
"eighty",
"ninety" ]

written_cases = []
for num in written_numbers:
    written_cases.append("chapter " + num)

print written_cases


def chapter_format_identifier():
    """ Chooses how to parse the file on chapters.
    """

    with open(filename, 'r') as f:
        contents = f.read()

    pattern = 'chapter.....'
    matches = re.findall(pattern, contents)

    # test for written numbers
    written_counter = 0
    written_matches = []
    for poss_match in written_cases:
        if re.search(poss_match, contents, flags=re.IGNORECASE) is not None:
            written_counter += 1

    return written_cases

def chapter_splitter(cases):
    """ This function accepts a list and iteratively attempts to parse on each item
    until none more are returned.

    Note for future:
    It is possible to prevent false matches by using an incrementing sequence
    when parsing on each chapter format instance.
    """

    with open(filename, 'r') as f:
        contents = f.read()

    filename_incrementer = 0
    prev_chapter_string = ""
    for match in cases:

        matched = True
        while matched == True:

            # We want to split everything before the match and send it to a new file.
            # (And everything after the previous match)
            matched_split = re.split("("+match+")", contents, maxsplit=1, flags=re.IGNORECASE)
            if len(matched_split) == 3:

                print matched_split[1]
                contents = matched_split[2]
                
                partial_file_filename = filename+str(filename_incrementer)
                with open(partial_file_filename, 'w') as f:
                    f.write(prev_chapter_string+matched_split[0])

                prev_chapter_string = matched_split[1]
                filename_incrementer += 1

            else:
                matched = False
            


if __name__ == '__main__':

    cases = chapter_format_identifier()

    print cases

    chapter_splitter(cases)



