"""Unittest for file line_count.py"""

import unittest
from unittest.mock import MagicMock
import line_count


class LineCountTest(unittest.TestCase):
    """
    Unittest for file line_count.py
    """

    def test_find_ext_under_path_without_subdirectory(self):
        """
        Test for find_ext_under_path. The testing directory has no subdirectory.
        """
        dir_path = "testing_without_subdirectory/"
        ext = ".txt"
        actual = line_count.find_ext_under_path(dir_path, ext)
        expected = [
            "testing_without_subdirectory/file3.txt",
            "testing_without_subdirectory/file1.txt",
            "testing_without_subdirectory/file4.txt",
        ]
        self.assertEqual(actual, expected)

    def test_find_ext_under_path_with_subdirectory(self):
        """
        Test for find_ext_under_path. The testing directory has nested subdirectories.
        """
        dir_path = "testing_with_subdirectory/"
        ext = ".txt"
        actual = line_count.find_ext_under_path(dir_path, ext)
        expected = [
            "testing_with_subdirectory/file3.txt",
            "testing_with_subdirectory/file1.txt",
            "testing_with_subdirectory/file4.txt",
            "testing_with_subdirectory/dir1/file3.txt",
            "testing_with_subdirectory/dir1/file1.txt",
            "testing_with_subdirectory/dir1/file4.txt",
            "testing_with_subdirectory/dir1/dir2/file3.txt",
            "testing_with_subdirectory/dir1/dir2/file1.txt",
            "testing_with_subdirectory/dir1/dir2/file4.txt",
        ]
        self.assertEqual(actual, expected)

    def test_find_ext_under_path_non_default_extension(self):
        """
        Test for find_ext_under_path. The file extension is .dummy instead of .txt.
        """
        dir_path = "testing_without_subdirectory/"
        ext = ".dummy"
        actual = line_count.find_ext_under_path(dir_path, ext)
        expected = [
            "testing_without_subdirectory/file1.dummy"
        ]
        self.assertEqual(actual, expected)

    def test_find_ext_under_path_empty_dir(self):
        """
        Test for find_ext_under_path. The dir is empty.
        """
        dir_path = "testing_empty_files/"
        ext = ".txt"
        actual = line_count.find_ext_under_path(dir_path, ext)
        expected = []
        self.assertEqual(actual, expected)

    def test_line_count(self):
        """
        Test for line_count. Counting for files ending with .txt.
        """
        dir_path = "testing_without_subdirectory/"
        ext = ".txt"
        files = [
            "testing_without_subdirectory/file3.txt",
            "testing_without_subdirectory/file1.txt",
            "testing_without_subdirectory/file4.txt",
        ]
        line_count.find_ext_under_path = MagicMock(return_value=files)
        actual = line_count.count_lines(dir_path, ext)
        expected = {
            "testing_without_subdirectory/file3.txt": 14,
            "testing_without_subdirectory/file1.txt": 10,
            "testing_without_subdirectory/file4.txt": 0,
        }
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
