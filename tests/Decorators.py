def logger(func):

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@logger
def hello():
    print("Hello")


class User:

    @staticmethod
    def add():
        pass

    @classmethod
    def create(cls):
        pass

    @property
    def name(self):
        return "EdgeForge"