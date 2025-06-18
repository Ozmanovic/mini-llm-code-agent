# tests.py

import unittest

from functions.get_files_info import write_file



class Test_get_file_content(unittest.TestCase):


    def test_get_file_content(self):
        result = write_file("calculator", "lorem.txt","wait, this isn't lorem ipsum")
        print("TEST 1: ")

        print(result)

        print("TEST 1 ")

    def test_get_files_content2(self):
        result = write_file("calculator", "pkg/morelorem.txt","lorem ipsum dolor sit amet")
        print("TEST2: ")

        print(result)

        print("TEST2: ")

    def test_get_files_content3(self):
        result = write_file("calculator", "/tmp/temp.txt","this should not be allowed")
        print("TEST3: ")

        print(result)

        print("TEST3: ")


if __name__ == "__main__":
    unittest.main()