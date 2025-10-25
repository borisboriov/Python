class BookNotAvailableException(Exception):
    def __init__(self, message: str = "Book is not available"):
        self.message = message
        super().__init__(self.message)
