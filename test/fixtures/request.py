ADD_INPUT_CASES = [

                    ({'id': '51', 'task': 's', 'description': None, 'deadline': None}, True),
                    ({'id': '6', 'task': 's', 'description': 's', 'deadline': None}, True),
                    ({'id': '7', 'task': 's', 'description': 's', 'deadline':  "2021-10-20-10:10"}, True)

                ]

LIST_INPUT_CASES = [

                    ({}, False),
                    ({'deadline': '2020-10-10-10:10'}, True)
                ]

DELETE_INPUT_CASES = [

                    ({'id': 100}, True),
                    ({'id': 1}, False)
                ]

UPDATE_INPUT_CASES = [

                    ({'id': 1}, False),
                    ({'id': 1, 'description': 's'}, True),
                    ({'id': 1, 'description': 's', 'deadline': "2021-10-20 10:10:00"}, True),
                    ({'id': 1, 'description': 's', 'deadline': "2021-10-20 10:10:00", '--title': 's'}, True)
                ]