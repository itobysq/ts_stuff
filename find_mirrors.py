"""
A module to open a file of words (in_file), find all words that are mirror images, and output them to out_file
"""


def find_mirrors(in_file, out_file):
    """
    A function to find words that are mirror images of each other. Palindromes are eliminated from
    consideration (line 20). Mirror image words are written to output.txt (Aaron/noraA\n). The
    algorithm works by iterating line by line through the file and comparing that line with the
    reverse of the previous line (previous_line[::-1]). If there's a match, the algorithm checks
    if the previous line is a palindrome and if it is not a palindrome,
    the pair is written to out_file.
    :param in_file: a list of words containing one word per line.
    :param out_file: A list of mirror image words containing one mirror pair per line.
    """
    previous_line = ''
    for line in in_file:
        line = line.strip()
        previous_line = previous_line.strip()

        if not previous_line:
            previous_line = line
        else:
            if previous_line == line[::-1]:
                if previous_line != previous_line[::-1]:
                    out_file.write(previous_line + ', ' + line + '\n')

            previous_line = line


with open("linuxwords", 'r') as in_file:

    with open('output.txt', 'w') as out_file:

        print(find_mirrors(in_file, out_file))
