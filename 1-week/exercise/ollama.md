**Explanation of the Code**

The provided code is a Python snippet that utilizes generators, iteration, and dictionary methods. Here's a breakdown of what it does:

```python
yield from {book.get('author') for book in books}
```

1. **Dictionary comprehension**: `{ book.get('author') for book in books }` creates an iterator that yields the values obtained by calling `get('author')` on each book object in the `books` collection.
   - The `.get()` method is used to retrieve a value from a dictionary (or, in this case, a book object) with an optional default value. If the key is not present or its value is `None`, it returns `None`.
2. **Generator expression**: This code uses a generator expression instead of a list comprehension for several reasons:
   - Memory efficiency: Generator expressions yield one item at a time, rather than computing all items and storing them in memory.
   - Infinite iteration support: Generators can be used to create infinite sequences by simply yielding more values indefinitely.

**Why this Code is Used**

The `yield from` expression is part of Python 3.3 and later versions.

It's used here to delegate the execution to a sub-generator, which is created by the dictionary comprehension. The `yield from` statement allows us to yield all items produced by the sub-generator.

In other words, this code iterates over each book object in the `books` collection, retrieves its author name using `.get('author')`, and then yields those values directly.

Here's an equivalent example without using generator expressions:

```python
for book in books:
    yield book.get('author')
```

This is more memory-efficient for large datasets but has a similar behavior to the original code.