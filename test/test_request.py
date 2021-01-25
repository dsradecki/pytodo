import unittest
from src.request import Add, Delete, Update, List
from test.fixtures import *


class TestAdd(unittest.TestCase):
    def test_add_request(self):
        for input_case, output_case in ADD_OUTPUT_CASES:
            add = Add(input_case)
            self.assertEqual(add.parser.parse_remove_args(input_case), True)


class TestRemove(unittest.TestCase):
    def test_add_request(self):
        for input_case, output_case in REMOVE_INPUT_CASES:
            add = Delete(input_case)
            self.assertEqual(add.parser.parse_remove_args(input_case), True)


class TestList(unittest.TestCase):
    def test_add_request(self):
        for input_case, output_case in LIST_INPUT_CASES:
            add = List(input_case)
            self.assertEqual(add.parser.parse_remove_args(input_case), True)


class TestUpdate(unittest.TestCase):
    def test_add_request(self):
        for input_case, output_case in REMOVE_INPUT_CASES:
            add = Update(input_case)
            self.assertEqual(add.parser.parse_remove_args(input_case), True)


if __name__ == '__main__':
    unittest.main()