## PYTHON - MORE DATA STRUCTURES: SET, DICTIONARY

### Sets:

A set is an unordered collection of unique elements in Python. It is defined using curly braces `{}` or the `set()` constructor. Sets automatically remove duplicate values, and they're often used to perform mathematical set operations.

**Usage:**

```python
my_set = {1, 2, 3, 4, 5}
```

### Common Set Methods and Usage:

1. **Adding Elements:**

```python
my_set.add(6)
```

2. **Removing Elements:**

```python
my_set.remove(3)
```

3. **Union of Sets:**

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
```

### Sets vs. Lists:

Use sets when you need to ensure uniqueness and don't care about order. Use lists when order matters and duplicates are allowed.

### Iterating Through a Set:

You can iterate through a set using a loop:

```python
for item in my_set:
    print(item)
```

### Dictionaries:

A dictionary is an unordered collection of key-value pairs. Each key must be unique and maps to a corresponding value. Dictionaries are created using curly braces `{}` with key-value pairs.

**Usage:**

```python
my_dict = {"name": "Alice", "age": 30}
```

### Common Dictionary Methods and Usage:

1. **Accessing Values:**

```python
name = my_dict["name"]
```

2. **Adding or Updating Items:**

```python
my_dict["city"] = "New York"
```

3. **Removing Items:**

```python
del my_dict["age"]
```

### Dictionaries vs. Lists or Sets:

Use dictionaries when you need to associate values with unique keys. Use lists for ordered collections and sets for unique, unordered collections.

### Dictionary Keys:

A key is a unique identifier for a value in a dictionary. Keys are used to access and manipulate values.

### Iterating Through a Dictionary:

You can iterate through a dictionary's keys, values, or key-value pairs using loops:

```python
for key in my_dict:
    print(key, my_dict[key])
```

### Lambda Function:

A lambda function is a small anonymous function defined with the `lambda` keyword. It can have any number of arguments but only one expression.

**Usage:**

```python
add = lambda x, y: x + y
result = add(3, 5)  # Result will be 8
```

### Map, Reduce, and Filter Functions:

These functions are part of Python's `functools` module:

- `map(function, iterable)`: Applies a function to all items in an iterable.
- `filter(function, iterable)`: Filters out items from an iterable based on a condition.
- `reduce(function, iterable)`: Applies a rolling computation to sequential pairs of items.

**Usage:**

```python
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
even_numbers = filter(lambda x: x % 2 == 0, numbers)
from functools import reduce
sum_result = reduce(lambda x, y: x + y, numbers)
```

These functions are useful for concise and expressive data transformations.