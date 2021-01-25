import unittest
from src.parser import Parser
from test.fixtures import ADD_INPUT_CASES, ADD_OUTPUT_CASES
from src.request import Add

from test.mock_database import MockDB
from mock import patch


class TestAdd(MockDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = Parser()

    def test_parse_add_args(self):
        for input_case, output_case in zip(ADD_INPUT_CASES, ADD_OUTPUT_CASES):
            self.assertEqual(self.parser.parse_add_args(input_case), output_case)

    def test_add_request(self):
        for input_case, output_case in ADD_OUTPUT_CASES:
            with self.mock_db_config:
                add_request = Add(input_case)
                self.assertEqual(add_request.perform_query(), True)


if __name__ == '__main__':
    unittest.main()
