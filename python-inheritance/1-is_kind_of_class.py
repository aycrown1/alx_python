"""
a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
"""
def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or an instance of a class inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        bool: True if the object is an instance of the specified class or its subclasses; otherwise False.
    """
    return isinstance(obj, a_class)