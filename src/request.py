from src.utils import perform_query


class Request():
    def __init__(self, body: dict):
        self.body = body


class Add(Request):
    def __init__(self, body: dict):
        super().__init__(body)

    def perform_query(self) -> bool:
        def generate_query():
            #change body (dictionary) to a particurlar SQL string here
            pass
        #return perform_query(SQL_query)


class Delete(Request):
    def __init__(self, body: dict):
        super().__init__(body)

    def perform_query(self) -> bool:
        def generate_query():
            #change body (dictionary) to a particurlar SQL string here
            pass
        #return perform_query(SQL_query)


class List(Request):
    def __init__(self, body: dict):
        super().__init__(body)

    def perform_query(self) -> bool:
        def generate_query():
            #change body (dictionary) to a particurlar SQL string here
            pass
        #return perform_query(SQL_query)


class Update(Request):
    def __init__(self, body: dict):
        super().__init__(body)

    def perform_query(self) -> bool:
        def generate_query():
            #change body (dictionary) to a particurlar SQL string here
            pass
        #return perform_query(SQL_query)
