### PYTHON - DATA STRUCTURE:LISTS, TUPLES

A Python data structure is a way of organizing and storing data in a specific format. Data structures provide a way to efficiently manage, access, and manipulate data. Python offers several built-in data structures that cater to different needs. Here are some common Python data structures, along with their creation, usage, and purposes:

 ### Lists:

A list is a ordered collection of items in Python. Lists can hold elements of different data types and are defined using square brackets `[]`. Lists are mutable, meaning you can modify their elements after creation.

**Usage:**

```python
my_list = [1, 2, 3, "hello", True]
```

### Differences and Similarities Between Strings and Lists:

- **Similarities:**
  - Both are sequences of items.
  - Both support indexing and slicing.
  - Both can be iterated through using loops.

- **Differences:**
  - Strings hold characters, while lists hold any type of elements.
  - Strings are immutable, while lists are mutable.

### Common List Methods and Usage:

1. **Appending Elements:**

```python
my_list.append(4)
```

2. **Inserting Elements:**

```python
my_list.insert(2, "world")
```

3. **Removing Elements:**

```python
my_list.remove("hello")
```

### Using Lists as Stacks and Queues:

- **Stacks:**
  - Use `append()` to push an item onto the stack.
  - Use `pop()` to remove and return the top item.

- **Queues:**
  - Use `append()` to enqueue an item.
  - Use `pop(0)` to dequeue the first item.

### List Comprehensions:

List comprehensions are concise ways to create lists. They allow you to apply an expression to each item in an iterable.

**Usage:**

```python
squared_numbers = [x ** 2 for x in range(1, 6)]
```

### Tuples:

A tuple is an ordered, immutable collection of items in Python. Tuples are defined using parentheses `()`.

**Usage:**

```python
my_tuple = (1, 2, 3, "hello")
```

### When to Use Tuples vs. Lists:

Use tuples when you want to create collections that should not be modified after creation. Lists are suitable for collections that need to be updated.

### Sequence:

A sequence is an ordered set of items. Both strings and lists are examples of sequences.

### Tuple Packing:

Tuple packing is creating a tuple by grouping items together within parentheses.

```python
point = 2, 3
```

### Sequence Unpacking:

Sequence unpacking is assigning values from a sequence to multiple variables.

```python
x, y = point
```

### The `del` Statement:

The `del` statement removes an item from a list by its index or deletes a variable.

**Usage:**

```python
del my_list[2]
```

In a summary, lists are ordered collections of items, and they can be used for various purposes. Strings and lists share sequence-like properties. Common list methods include appending, inserting, and removing items. Lists can be used as stacks and queues. List comprehensions provide a concise way to create lists. Tuples are similar to lists, but they are immutable. Sequence packing and unpacking allow efficient assignment and access of values. The `del` statement can be used to remove items from lists or delete variables.