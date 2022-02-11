class ClientException(Exception):
    """ Class responsable for custom exceptions"""

    def __init__(self, status_code, message='Request error'):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)