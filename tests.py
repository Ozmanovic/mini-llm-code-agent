# tests.py

import unittest

from functions.run_python import run_python_file



class Test_get_file_content(unittest.TestCase):


    def test_get_file_content(self):
        result = run_python_file("calculator", "main.py")
        print("TEST 1: ")

        print(result)

        print("TEST 1 ")

    def test_get_files_content2(self):
        result = run_python_file("calculator", "tests.py")
        print("TEST2: ")

        print(result)

        print("TEST2: ")

    def test_get_files_content3(self):
        result = run_python_file("calculator", "../main.py")
        print("TEST3: ")

        print(result)

        print("TEST3: ")

    def test_get_files_content4(self):
        result = run_python_file("calculator", "nonexistent.py")
        print("TEST3: ")

        print(result)

        print("TEST3: ")



if __name__ == "__main__":
    unittest.main()