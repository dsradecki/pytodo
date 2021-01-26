import unittest
from test.fixtures.request import ADD_INPUT_CASES, DELETE_INPUT_CASES, UPDATE_INPUT_CASES, LIST_INPUT_CASES
from src.request import Add, Delete, Update, List

from test.mock_database import MockDB
import nose.tools


class TestAdd(MockDB):

    def test_add(self):
        with self.mock_db_config:
            for add_input, output in ADD_INPUT_CASES:
                with self.subTest(query=add_input):
                    add_request = Add(add_input, 'tasks')

                    self.assertEqual(add_request.perform_query(), output)

    def test_delete_request(self):
        with self.mock_db_config:
            for input_case, output_case in DELETE_INPUT_CASES:
                with self.subTest(query=input_case):
                    delete_request = Delete(input_case, 'tasks')
                    self.assertEqual(delete_request.perform_query(), output_case)

    def test_list_request(self):
        with self.mock_db_config:
            for input_case, output_case in LIST_INPUT_CASES:
                with self.subTest(query=input_case):
                    list_request = List(input_case, 'tasks')
                    self.assertEqual(list_request.perform_query(), output_case)

    def test_update_request(self):
        with self.mock_db_config:
            for input_case, output_case in UPDATE_INPUT_CASES:
                with self.subTest(query=input_case):
                    update_request = Update(input_case, 'tasks')
                    self.assertEqual(update_request.perform_query(), output_case)

