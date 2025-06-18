# tests.py

import unittest

from functions.get_files_info import get_file_content



class Test_get_file_content(unittest.TestCase):


    def test_get_file_content(self):
        result = get_file_content("calculator", "main.py")
        print("THIS SHOULD BE MAIN.PY CODE: ")
        print(result)
        print("THIS SHOULD BE MAIN.PY CODE: ")

    def test_get_files_content2(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print("THIS SHOULD BE CALCULATOR.PY CODE: ")
        print(result)
        print("THIS SHOULD BE CALCULATOR.PY CODE: ")
    def test_get_files_content3(self):
        result = get_file_content("calculator", "/bin/cat")
        print("THIS SHOULD BE ERROR: ")
        print(result)
        print("THIS SHOULD BE ERROR: ")


if __name__ == "__main__":
    unittest.main()