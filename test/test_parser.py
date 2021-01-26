import unittest

from src.parser import Parser
from test.fixtures.parser import ADD_INPUT_CASES, ADD_OUTPUT_CASES, DELETE_INPUT_CASES, DELETE_OUTPUT_CASES, \
    LIST_INPUT_CASES, LIST_OUTPUT_CASES, UPDATE_INPUT_CASES, UPDATE_OUTPUT_CASES


class TestParser(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = Parser()

    def test_parse_add_args(self):
        for input, output in zip(ADD_INPUT_CASES, ADD_OUTPUT_CASES):
            with self.subTest(query=input):
                self.assertEqual(self.parser.parse_add_args(input), output)

    def test_parse_remove_args(self):
        for input, output in zip(DELETE_INPUT_CASES, DELETE_OUTPUT_CASES):
            with self.subTest(query=input):
                self.assertEqual(self.parser.parse_delete_args(input), output)

    def test_parse_list_args(self):
        for input, output in zip(LIST_INPUT_CASES, LIST_OUTPUT_CASES):
            with self.subTest(query=input):
                self.assertEqual(self.parser.parse_list_args(input), output)

    def test_parse_update_args(self):
        for input, output in zip(UPDATE_INPUT_CASES, UPDATE_OUTPUT_CASES):
            with self.subTest(query=input):
                self.assertEqual(self.parser.parse_update_args(input), output)


if __name__ == '__main__':
    unittest.main()