ADD_INPUT_CASES = [
                    ['--title', 's'],
                    ['--title', 's', '--description', 's'],
                    ['--title', 's', '--description', 's', '--deadline', '20-10-2021-10:10'],
                ]

UPDATE_INPUT_CASES = [

                    ['--id', 1],
                    ['--id', 1, '--description', 's'],
                    ['--id', 1, '--description', 's', 'deadline', '20-10-2021-10:10'],
                    ['--id', 1, '--description', 's', 'deadline', '20-10-2021-10:10', '--title', 's'],
                ]

REMOVE_INPUT_CASES = [

                    ['--id', 1],
                ]

LIST_INPUT_CASES = [

                    [],
                    ['--deadline', '2020-10-10-10:10'],
                ]

ADD_OUTPUT_CASES = [

                    {'title': 's', 'description': None, 'deadline': 'Null'},
                    {'title': 's', 'description': 's', 'deadline': 'Null'},
                    {'title': 's', 'description': 's', 'deadline':  "'2021-10-20 10:10:00'"}

                ]

LIST_OUTPUT_CASES = [

                    {},
                    {'deadline': '2020-10-10-10:10'}
                ]

REMOVE_OUTPUT_CASES = [

                    {'id': 1}
                ]

UPDATE_OUTPUT_CASES = [

                    {'id': 1},
                    {'id': 1, 'description': 's'},
                    {'id': 1, 'description': 's', 'deadline': "'2021-10-20 10:10:00'"},
                    {'id': 1, 'description': 's', 'deadline': "'2021-10-20 10:10:00'", '--title': 's'}
                ]
