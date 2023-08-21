### PYTHON CLASS

### Object-Oriented Programming (OOP):

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects, each representing a real-world entity. OOP focuses on designing classes to encapsulate data and methods that operate on the data. It promotes code reusability, modularity, and abstraction.

### "First-Class Everything":

In Python, "first-class everything" means that all entities (variables, functions, classes, etc.) are treated as objects with the same privileges and capabilities. They can be passed around, assigned, and manipulated like any other object.

### Class:

A class is a blueprint for creating objects. It defines attributes (data) and methods (functions) that objects of that class will have.

### Object and Instance:

An object is a specific instance of a class. "Instance" and "object" are often used interchangeably.

### Difference between a Class and an Object/Instance:

A class is a template or blueprint, while an object/instance is a concrete instantiation of that template.

### Attribute:

An attribute is a value associated with an object. Attributes can be data (variables) or methods (functions) associated with a class.

### Public, Protected, and Private Attributes:

- Public attributes are accessible from anywhere.
- Protected attributes are conventionally marked with a single leading underscore (`_`). They are meant to be accessed within the class and subclasses.
- Private attributes are conventionally marked with a double leading underscore (`__`). They are meant to be accessed only within the class that defines them.

### `self`:

`self` is a reference to the instance of the class. It is used within class methods to refer to the instance itself.

### Method:

A method is a function defined within a class that operates on its instances.

### `__init__` Method:

The `__init__` method is a special method used to initialize the attributes of an object when it is created.

### Data Abstraction, Data Encapsulation, and Information Hiding:

- **Data Abstraction:** Presenting only essential attributes and methods to the outside world while hiding the implementation details.
- **Data Encapsulation:** Wrapping data and methods into a single unit (a class), controlling access through methods.
- **Information Hiding:** Restricting access to certain attributes or methods to prevent accidental misuse.

### Property:

A property is a special attribute accessed using getter and setter methods. It allows control over access to an attribute.

### Attribute vs. Property in Python:

An attribute is a value associated with an object. A property is a special attribute accessed using getter and setter methods.

### Pythonic Way for Getters and Setters:

Python uses properties to create getters and setters, making attribute access more controlled.

### Dynamically Creating Attributes:

You can dynamically add attributes to instances using dot notation or the `setattr()` function.

### Binding Attributes to Objects and Classes:

Attributes are bound to instances or classes using dot notation.

### `__dict__`:

`__dict__` is a dictionary containing the attributes of a class or instance.

### Attribute Lookup:

Python searches the instance, then the class, and finally its parent classes to find attributes.

### Using `getattr` Function:

The `getattr(object, attribute)` function is used to get the value of an attribute. It returns an attribute's value if it exists, otherwise raises an error.

In Python, OOP provides a powerful and organized way to design and structure code, promoting modularity and code reuse.



Base on the python class we created for this project:

```markdown
# Square Class

This class defines a square shape with various attributes and methods.

## Attributes

- `__size` (int): Represents the size of the square.

## Constructor

```python
def __init__(self, size=0)
```

- Initializes a new instance of the `Square` class.
- Args:
  - `size` (int, optional): The size of the square. Defaults to 0.
- Raises:
  - `TypeError`: If `size` is not an integer.
  - `ValueError`: If `size` is less than 0.

## Properties

### size

- Property to retrieve the size of the square.
- Getter:
  ```python
  @property
  def size(self)
  ```
- Setter:
  ```python
  @size.setter
  def size(self, value)
  ```
- Raises:
  - `TypeError`: If `value` is not an integer.
  - `ValueError`: If `value` is less than 0.

## Methods

### area

```python
def area(self)
```

- Calculates and returns the area of the square.
- Returns:
  - `int`: The area of the square.

### my_print

```python
def my_print(self)
```

- Prints the square using the '#' character.
- If `size` is equal to 0, an empty line is printed.

