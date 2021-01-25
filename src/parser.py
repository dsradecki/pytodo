from argparse import ArgumentParser
from src.request import Request


class Parser():

    """
        Parser based on argparse with the following functionalities:

            - add --name STRING [--deadline DATETIME] [--description STRING]
            - remove --id
            - list [--deadline DATE]
            - update --id [--name STRING] [--deadline DATETIME] [--description STRING]
    """

    def __init__(self):
        self.parser = ArgumentParser()
        self.subparser = self.parser.add_subparsers(dest='command')

        self.dict_generators = {
            'add': self.parse_add_args,
            'remove': self.parse_update_args,
            'update': self.parse_list_args,
            'list': self.parse_remove_args
        }

    # GENERATOR METHODS, WHICH CONFIGURE AND RETURN REQUIRED PARSERS - ADD/REMOVE/LIST/UPDATE

    def generate_add_parser(self) -> ArgumentParser:
        pass

    def generate_delete_parser(self) -> ArgumentParser:
        pass

    def generate_list_parser(self) -> ArgumentParser:
        pass

    def generate_update_parser(self) -> ArgumentParser:
        pass

    # PARSING METHODS WHICH EMPLOY THE GENERATORS AND PARSE ARGS

    def parse_add_args(self, args: list) -> dict:
        pass

    def parse_delete_args(self, args: list) -> dict:
        pass

    def parse_update_args(self, args: list) -> dict:
        pass

    def parse_list_args(self, args: list) -> dict:
        pass

    # GENERAL PARSING METHOD

    def parse_args(self, sys_args: list) -> Request:
        command = sys_args[0]
        options = sys_args[1:]

        args = vars(self.dict_generators[command](options))

        print(args)

        request_constructor = globals()[command]
        request = request_constructor(args)

        return request


