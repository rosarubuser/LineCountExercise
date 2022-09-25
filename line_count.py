"""Line count for files ending with ext under the given directory"""

import os
from typing import Dict, List
from collections import deque


def count_lines(dir_path: str, ext: str) -> Dict[str, int]:
    """
    Count Lines for each file ending with ext under the given directory.
    """
    path_to_lines = {}
    files = find_ext_under_path(dir_path, ext)
    for file in files:
        with open(file, 'r') as input_file:
            path_to_lines[file] = len(input_file.readlines())
    return path_to_lines


def find_ext_under_path(dir_path: str, ext: str) -> List[str]:
    """
    Find all files under dir_path ending with ext.
    """
    dirs = deque([dir_path])
    paths = []
    while dirs:
        curr_d = dirs.pop()
        for file in os.listdir(curr_d):
            full_path = os.path.join(curr_d, file)
            if os.path.isfile(full_path) and file.endswith(ext):
                paths.append(full_path)
            elif os.path.isdir(full_path):
                dirs.append(full_path)

    return paths
