import unittest
from src.parser import Parser
from test.fixtures import UPDATE_OUTPUT_CASES, UPDATE_INPUT_CASES
from src.request import Update

from test.mock_database import MockDB
from mock import patch


class TestList(MockDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = Parser()

    def test_parse_list_args(self):
        for input_case, output_case in zip(UPDATE_INPUT_CASES, UPDATE_OUTPUT_CASES):
            self.assertEqual(self.parser.parse_list_args(input_case), output_case)

    def test_update_request(self):
        for input_case, output_case in UPDATE_INPUT_CASES:
            with self.mock_db_config:
                update_request = Update(input_case)
                self.assertEqual(update_request.perform_query(), True)


if __name__ == '__main__':
    unittest.main()