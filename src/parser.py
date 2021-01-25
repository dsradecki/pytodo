import argparse


class Parser():

    """
        Parser based on argparse with the following functionalities:

            - add --name STRING [--deadline DATETIME] [--description STRING]
            - remove --id
            - list [--deadline DATE]
            - update --id [--name STRING] [--deadline DATETIME] [--description STRING]
    """

    def __init__(self):
        pass

    # GENERATOR METHODS, WHICH CONFIGURE AND RETURN REQUIRED PARSERS - ADD/REMOVE/LIST/UPDATE

    def generate_add_parser(self) -> argparse.subparser:
        pass

    def generate_remover_parser(self) -> argparse.subparser:
        pass

    def generate_list_parser(self) -> argparse.subparser:
        pass

    def generate_update_parser(self) -> argparse.subparser:
        pass

    # PARSING METHODS WHICH EMPLOY THE GENERATORS AND PARSE ARGS

    def parse_add_args(self, args: list) -> dict:
        pass

    def parse_remove_args(self, args: list) -> dict:
        pass

    def parse_update_args(self, args: list) -> dict:
        pass

    def parse_list_args(self, args: list) -> dict:
        pass

    # GENERAL PARSING METHOD

    def parse_args(self, sys_args: list) -> Request:
        pass


