PARSE_ADD_INPUT_CASES = [
                    ['--title', 's'],
                    ['--title', 's', '--description', 's'],
                    ['--title', 's', '--description', 's', '--deadline', '20-10-2021-10:10'],
                ]

PARSE_ADD_OUTPUT_CASES = [

                    {'title': 's', 'description': 'Null', 'deadline': 'Null'},
                    {'title': 's', 'description': 's', 'deadline': 'Null'},
                    {'title': 's', 'description': 's', 'deadline':  "'2021-10-20 10:10:00'"}

                ]

QUERY_ADD_INPUT_CASES = [

                    {'id': '1', 'title': 's', 'description': 'Null', 'deadline': 'Null'},
                    {'id': '1', 'title': 's', 'description': 's', 'deadline': 'Null'},
                    {'id': '1', 'title': 's', 'description': 's', 'deadline':  "'2021-10-20 10:10:00'"}

                ]

UPDATE_INPUT_CASES = [

                    ['--id', 1],
                    ['--id', 1, '--description', 's'],
                    ['--id', 1, '--description', 's', 'deadline', '20-10-2021-10:10'],
                    ['--id', 1, '--description', 's', 'deadline', '20-10-2021-10:10', '--title', 's'],
                ]

DELETE_INPUT_CASES = [

                    ['--id', 1],
                ]

LIST_INPUT_CASES = [

                    [],
                    ['--deadline', '2020-10-10-10:10'],
                ]

LIST_OUTPUT_CASES = [

                    {},
                    {'deadline': '2020-10-10-10:10'}
                ]

DELETE_OUTPUT_CASES = [

                    {'id': 1}
                ]

UPDATE_OUTPUT_CASES = [

                    {'id': 1},
                    {'id': 1, 'description': 's'},
                    {'id': 1, 'description': 's', 'deadline': "'2021-10-20 10:10:00'"},
                    {'id': 1, 'description': 's', 'deadline': "'2021-10-20 10:10:00'", '--title': 's'}
                ]
