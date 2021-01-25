import unittest
from src.parser import Parser
from test.fixtures import DELETE_INPUT_CASES, DELETE_OUTPUT_CASES
from src.request import Delete

from test.mock_database import MockDB
from mock import patch


class TestDelete(MockDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = Parser()

    def test_parse_remove_args(self):
        for input_case, output_case in zip(DELETE_INPUT_CASES, DELETE_OUTPUT_CASES):
            self.assertEqual(self.parser.parse_delete_args(input_case), output_case)

    def test_delete_request(self):
        for input_case, output_case in DELETE_INPUT_CASES:
            with self.mock_db_config:
                delete_request = Delete(input_case)
                self.assertEqual(delete_request.perform_query(), True)


if __name__ == '__main__':
    unittest.main()