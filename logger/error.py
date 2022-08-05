class SerializeError(RuntimeError):
    pass


class PrintError(Exception):
    pass


class InitTypeError(TypeError):
    pass


class Testing(Warning):
    D_MESSAGE = 'This function has known problems.'

    def __init__(self, message: str = None):
        if message is None:
            self.message = self.D_MESSAGE
        else:
            self.message = message

    def __str__(self):
        return self.message
