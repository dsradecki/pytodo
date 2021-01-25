import unittest
from src.parser import Parser
from fixtures import ADD_INPUT_CASES, ADD_OUTPUT_CASES
from requests import Add


class TestAdd(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = Parser()

    def test_parse_add_args(self):
        for input_case, output_case in zip(ADD_INPUT_CASES, ADD_OUTPUT_CASES):
            self.assertEqual(self.parser.parse_add_args(input_case), output_case)

    def test_add_request(self):
        for input_case, output_case in ADD_OUTPUT_CASES:
            add_request = Add(input_case)
            self.assertEqual(add_request.perform_query(), True)


if __name__ == '__main__':
    unittest.main()
