from src.utils import write_to_db, read_from_db, generate_hash


class Request():
    def __init__(self, body: dict):
        self.body = body


class Add(Request):
    def __init__(self, body: dict):
        super().__init__(body)
        self.body['id'] = generate_hash(body['title'])

    def perform_query(self) -> bool:
        def generate_query():
            return "INSERT INTO tasks VALUES ({}) ".format(", ".join(self.body.values()))
        print(generate_query())
        return write_to_db(generate_query())


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
