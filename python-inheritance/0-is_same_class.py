#!/usr/bin/python3
"""
This module provides a function to check if an object is exactly an instance of a specified class.
"""
def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        bool: True if the object is an instance of the specified class; otherwise False.
    """
    return type(obj) is a_class