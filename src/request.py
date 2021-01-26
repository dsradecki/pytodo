from src.utils import write_to_db, read_from_db, generate_hash, generate_insert_query


class Request():
    def __init__(self, body: dict):
        self.body = body


class Add(Request):
    def __init__(self, body: dict):
        super().__init__(body)
        #ADD HASH - it has to be at first position and dictionaries are unordered...
        #REFACTOR THIS TO TWO ARGUMENTS BODY AND HASH...
        self.body = {'id': generate_hash(self.body['task']), **self.body}

    def perform_query(self) -> bool:
        query = generate_insert_query(self.body)
        return write_to_db(query, list(self.body.values()))


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
