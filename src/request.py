class Request():
    def __init__(self, body: dict):
        self.body = body


class Add(Request):
    def __init__(self, body: dict):
        super().__init__(body)


class Delete(Request):
    def __init__(self, body: dict):
        super().__init__(body)


class List(Request):
    def __init__(self, body: dict):
        super().__init__(body)


class Update(Request):
    def __init__(self, body: dict):
        super().__init__(body)
