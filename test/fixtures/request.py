ADD_INPUT_CASES = [

                    ({'id': '51', 'task': 's', 'description': None, 'deadline': None}, True),
                    ({'id': '6', 'task': 's', 'description': 's', 'deadline': None}, True),
                    ({'id': '7', 'task': 's', 'description': 's', 'deadline':  "'2021-10-20-10:10'"}, True)

                ]

LIST_INPUT_CASES = [

                    {},
                    {'deadline': '2020-10-10-10:10'}
                ]

DELETE_INPUT_CASES = [

                    {'id': 1}
                ]

UPDATE_INPUT_CASES = [

                    {'id': 1},
                    {'id': 1, 'description': 's'},
                    {'id': 1, 'description': 's', 'deadline': "'2021-10-20 10:10:00'"},
                    {'id': 1, 'description': 's', 'deadline': "'2021-10-20 10:10:00'", '--title': 's'}
                ]