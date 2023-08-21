## Python - Inheritance
### Superclass, Baseclass, or Parentclass:

A superclass, baseclass, or parentclass is a class from which other classes are derived. It serves as a template for creating more specialized classes.

### Subclass:

A subclass is a class that is derived from another class, known as its superclass. The subclass inherits attributes and methods from its superclass.

### Listing Attributes and Methods:

You can use the `dir()` function to list attributes and methods of a class or instance. For a more readable output, you can use the `vars()` function.

### Instance with New Attributes:

An instance can have new attributes assigned dynamically using dot notation or the `setattr()` function.

### Inheriting from Another Class:

To inherit from another class, include the superclass name in parentheses after the subclass name.

```python
class Subclass(Superclass):
    # Subclass attributes and methods here
```

### Defining a Class with Multiple Base Classes (Multiple Inheritance):

Multiple inheritance is achieved by listing multiple superclass names in the parentheses after the subclass name.

```python
class Subclass(BaseClass1, BaseClass2):
    # Subclass attributes and methods here
```

### Default Class Every Class Inherit From:

Every class in Python implicitly inherits from the `object` class, which is the root of the class hierarchy.

### Method or Attribute Override:

To override a method or attribute inherited from the base class, redefine it in the subclass. The overridden method will be called from the subclass instances.

### Available Attributes/Methods for Subclasses:

Subclasses inherit all attributes and methods (except private ones) from their superclass. They can also define their own additional attributes and methods.

### Purpose of Inheritance:

Inheritance allows code reuse, promotes modularity, and facilitates creating specialized classes based on existing ones.

### Built-in Functions for Inheritance and Type Checking:

- `isinstance(object, class_or_tuple)`: Checks if an object is an instance of a class or any class in a tuple.
- `issubclass(class, classinfo)`: Checks if a class is a subclass of another class or a class in a tuple.
- `type(object)`: Returns the type of an object.
- `super(subclass, instance)`: Returns a temporary object that provides access to inherited methods.

These built-in functions help you determine class relationships, perform type checks, and manage inheritance.