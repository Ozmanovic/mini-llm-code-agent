# tests.py

import unittest

from functions.get_files_info import get_files_info



class Test_get_files_info(unittest.TestCase):


    def test_get_files_info1(self):
        result = get_files_info("calculator", ".")
        print(result)

    def test_get_files_info2(self):
        result = get_files_info("calculator", "pkg")
        print(result)

    def test_get_files_info3(self):
        result = get_files_info("calculator", "/bin")
        print(result)       

    def test_get_files_info4(self):
        result = get_files_info("calculator", "../")
        print(result)


if __name__ == "__main__":
    unittest.main()