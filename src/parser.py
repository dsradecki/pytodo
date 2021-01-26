from argparse import ArgumentParser
from src.request import Request, Add, Delete, Update, List
from src.utils import valid_datetime, valid_date


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
            'delete': self.parse_delete_args,
            'update': self.parse_update_args,
            'list': self.parse_list_args
        }

    # GENERATOR METHODS, WHICH CONFIGURE AND RETURN REQUIRED PARSERS - ADD/REMOVE/LIST/UPDATE

    def generate_add_parser(self) -> ArgumentParser:
        add_parser = self.subparser.add_parser('add',
                                               help='Add a new task'
                                               )
        add_parser.add_argument('--task',
                                metavar='title',
                                required=True,
                                type=str,
                                )
        add_parser.add_argument('--description',
                                metavar='description',
                                type=str,
                                default=None
                                )
        add_parser.add_argument('--deadline',
                                metavar='deadline',
                                type=valid_datetime,
                                default=None
                                )

        return add_parser

    def generate_delete_parser(self) -> ArgumentParser:
        remove_parser = self.subparser.add_parser('delete')

        remove_parser.add_argument('--id',
                                   metavar='id',
                                   required=True)

        return remove_parser

    def generate_list_parser(self) -> ArgumentParser:
        list_parser = self.subparser.add_parser('list',
                                                help='Add a new task')
        list_parser.add_argument('--deadline',
                                 metavar='deadline',
                                 default='Null',
                                 type=valid_date)

        return list_parser

    def generate_update_parser(self) -> ArgumentParser:
        update_parser = self.subparser.add_parser('update')

        update_parser.add_argument('--task',
                                   metavar='title',
                                   default=None,
                                   type=str)
        update_parser.add_argument('--deadline',
                                   metavar='deadline',
                                   default=None,
                                   type=valid_date)
        update_parser.add_argument('--description',
                                   metavar='description',
                                   default=None)
        update_parser.add_argument('--id',
                                   metavar='id',
                                   type=str,
                                   required=True)

        return update_parser

    # PARSING METHODS WHICH EMPLOY THE GENERATORS AND PARSE ARGS

    def parse_add_args(self, args: list) -> dict:
        add_parser = self.generate_add_parser()
        return vars(add_parser.parse_args(args))

    def parse_delete_args(self, args: list) -> dict:
        remove_parser = self.generate_delete_parser()
        return vars(remove_parser.parse_args(args))

    def parse_update_args(self, args: list) -> dict:
        update_parser = self.generate_update_parser()
        return vars(update_parser.parse_args(args))

    def parse_list_args(self, args: list) -> dict:
        list_parser = self.generate_list_parser()
        return vars(list_parser.parse_args(args))

    # GENERAL PARSING METHOD

    def parse_args(self, sys_args: list, table) -> Request:
        command = sys_args[0]
        options = sys_args[1:]
        args = self.dict_generators[command](options)

        request_constructor = globals()[command.capitalize()]
        request = request_constructor(args, table)

        return request
