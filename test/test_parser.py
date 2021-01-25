import unittest
from parser import Parser
from fixtures import ADD_INPUT_CASES, ADD_OUTPUT_CASES, REMOVE_INPUT_CASES, REMOVE_OUTPUT_CASES, \
                        LIST_INPUT_CASES, LIST_OUTPUT_CASES, UPDATE_INPUT_CASES, UPDATE_OUTPUT_CASES


class TestParser(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = Parser()

    def test_parse_remove_args(self):
        for input_case, output_case in zip(REMOVE_INPUT_CASES, REMOVE_OUTPUT_CASES):
            self.assertEqual(self.parser.parse_remove_args(input_case), output_case)

    def test_parse_update_args(self):
        for input_case, output_case in zip(UPDATE_INPUT_CASES, UPDATE_OUTPUT_CASES):
            self.assertEqual(self.parser.parse_update_args(input_case), output_case)

    def test_parse_list_args(self):
        for input_case, output_case in zip(LIST_INPUT_CASES, LIST_OUTPUT_CASES):
            self.assertEqual(self.parser.parse_list_args(input_case), output_case)

    def test_parse_add_args(self):
        for input_case, output_case in zip(ADD_INPUT_CASES, ADD_OUTPUT_CASES):
            self.assertEqual(self.parser.parse_add_args(input_case), output_case)


if __name__ == '__main__':
    unittest.main()