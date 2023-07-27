#!/use/bin/python3
def raise_exception():
    """
    Raises a custom type exception.
    """
    class CustomException(Exception):
        pass

    raise CustomException("This is a custom exception.")