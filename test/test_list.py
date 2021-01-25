import unittest
from src.parser import Parser
from test.fixtures import LIST_OUTPUT_CASES, LIST_INPUT_CASES
from src.request import List


class TestList(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = Parser()

    def test_parse_list_args(self):
        for input_case, output_case in zip(LIST_INPUT_CASES, LIST_OUTPUT_CASES):
            self.assertEqual(self.parser.parse_list_args(input_case), output_case)

    def test_list_request(self):
        for input_case, output_case in LIST_INPUT_CASES:
            list_request = List(input_case)
            self.assertEqual(list_request.perform_query(), True)


if __name__ == '__main__':
    unittest.main()