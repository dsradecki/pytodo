import unittest
from src.parser import Parser
from test.fixtures import LIST_OUTPUT_CASES, LIST_INPUT_CASES
from src.request import List

from test.mock_database import MockDB
from mock import patch


class TestList(MockDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = Parser()

    def test_parse_list_args(self):
        for input_case, output_case in zip(LIST_INPUT_CASES, LIST_OUTPUT_CASES):
            self.assertEqual(self.parser.parse_list_args(input_case), output_case)

    def test_list_request(self):
        for input_case, output_case in LIST_INPUT_CASES:
            with self.mock_db_config:
                list_request = List(input_case)
                self.assertEqual(list_request.perform_query(), True)


if __name__ == '__main__':
    unittest.main()