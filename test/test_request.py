import unittest
from test.fixtures.request import ADD_INPUT_CASES, DELETE_INPUT_CASES, UPDATE_INPUT_CASES, LIST_INPUT_CASES
from src.request import Add, Delete, Update, List

from test.mock_database import MockDB
import nose.tools


class TestAdd(MockDB):

    def setUp(self):

        for add_input, output in ADD_INPUT_CASES:
            setattr(TestAdd, 'test_expected_%d' % output, self.test_add_request(add_input, output))

    def test_add_request(self, add_input, add_output):
        with self.mock_db_config:
            add_request = Add(add_input)
            print(add_input)
            return self.assertEqual(add_request.perform_query(), add_output)

    """"
    def test_delete_request(self):
        for input_case, output_case in DELETE_INPUT_CASES:
            with self.mock_db_config:
                delete_request = Delete(input_case)
                yield nose.tools.assert_equals, delete_request.perform_query(), True

    def test_list_request(self):
        for input_case in LIST_INPUT_CASES:
            with self.mock_db_config:
                list_request = List(input_case)
                yield nose.tools.assert_equals, list_request.perform_query(), True

    def test_update_request(self):
        for input_case, output_case in UPDATE_INPUT_CASES:
            with self.mock_db_config:
                update_request = Update(input_case)
                yield nose.tools.assert_equals, update_request.perform_query(), True
    """

if __name__ == '__main__':
    unittest.main()
