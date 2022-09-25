"""CLI for line_count.py"""

import os
import argparse
from typing import Dict, Tuple
from line_count import count_lines


def get_args() -> Tuple[str, str]:
    """
    Get command line arguments. Return the directory path and target file extension.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="path to directory")
    parser.add_argument("-e", "--extension", type=str, help="file extension", default=".txt")

    args = parser.parse_args()
    input_path = args.path
    if not os.path.isdir(input_path):
        raise Exception("invalid path")

    return input_path, args.extension


def print_results(path_to_lines: Dict[str, int]) -> None:
    """
    Print file counts, # of files, total lines, and average line count in terminal.
    """
    file_num = len(path_to_lines)
    lines_tot = 0
    for curr_p, cnt in path_to_lines.items():
        print("{:<55} {:<10}".format(curr_p, cnt))
        lines_tot += cnt
    print("=" * 55)
    print("Number of files found:   {}".format(file_num))
    print("Total number of lines:   {}".format(lines_tot))
    print("Average lines per file:  {:.2f}".format(lines_tot / file_num))


path, ext = get_args()
pathToLines = count_lines(path, ext)
print_results(pathToLines)
