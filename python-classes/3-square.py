#!/usr/bin/python3
"""
This module defines the Square class.
Classes:
    Square: Represents a square shape.
"""
class Square:
    """
    This class defines a square.
    
    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.
        
        Args:
            size (int, optional): The size of the square. Defaults to 0.
            
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size
    
    @property
    def size(self):
        """
        Get the size of the square.
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        Set the size of the square.
        
        Args:
            value (int): The new size of the square.
            
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """
        Calculates and returns the current square area.
        
        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size