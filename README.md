# Pretty Repr
Like repr but pretty.

A Python function that returns the Python representation of an object, formatted nicely. No dependencies. The parameters are very similar to json.dumps().

`pretty_repr_lite` is an ultra-lightweight version of the function that is easier to understand and adapt to specific usecases.

## Parameters
- ``skipkeys``: ``dict`` keys that are not basic types (``str``, ``int``, ``float``, ``bool``, ``None``) will be skipped.
- ``indent``: The level of indentation to use. If a string is specified, it will be used as the indentation.
- ``separators``: Should be an ``(item_separator, key_separator)`` tuple. The default is ``(', ', ': ')`` if ``indent`` is ``None`` and ``(',', ': ')`` otherwise.
- ``sort_keys``: Sort the output of dictionaries by key.

## Notes
### Production safe?
Who knows? It is working perfectly for all my usecases. There is a tests.py file which you could adapt to check that it will return a proper representation of the objects in your project.
### Speed?
It's quite fast. (I think) the Big O Notation is:
- `O(n)` if sort_keys is False.
- `O(m + n log n)` if sort_keys is True.

Where:
- n is the total number of elements in the input obj.
- m is the number of dictionaries that require sorting.