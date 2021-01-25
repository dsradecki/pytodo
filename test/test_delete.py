import unittest
from src.parser import Parser
from fixtures import DELETE_INPUT_CASES, DELETE_OUTPUT_CASES
from requests import Delete


class TestDelete(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = Parser()

    def test_parse_remove_args(self):
        for input_case, output_case in zip(DELETE_INPUT_CASES, DELETE_OUTPUT_CASES):
            self.assertEqual(self.parser.parse_remove_args(input_case), output_case)

    def test_add_request(self):
        for input_case, output_case in DELETE_INPUT_CASES:
            delete_request = Delete(input_case)
            self.assertEqual(delete_request.perform_query(), True)


if __name__ == '__main__':
    unittest.main()