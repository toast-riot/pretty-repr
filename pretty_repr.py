def pretty_repr(obj, skipkeys: bool = False, indent: int | str | None = None, separators: tuple[str, str] | None = None, sort_keys: bool = False) -> str:
    """Return a nicely formatted string representation of a Python object.

    Behaves similarly to ``json.dumps``.

    ``skipkeys``: ``dict`` keys that are not basic types (``str``, ``int``, ``float``, ``bool``, ``None``) will be skipped.

    ``indent``: The level of indentation to use. If a string is specified, it will be used as the indentation.

    ``separators``: Should be an ``(item_separator, key_separator)`` tuple. The default is ``(', ', ': ')`` if ``indent`` is ``None`` and ``(',', ': ')`` otherwise.

    ``sort_keys``: Sort the output of dictionaries by key.
    """

    newline = "" if indent is None else "\n"
    separators = separators or (", ", ": ") if indent is None else (",", ": ")
    indent = " " * indent if isinstance(indent, int) else indent or ""

    invalid_key = lambda k: skipkeys and not isinstance(k, (str, int, float, bool, type(None)))

    def encoder(key, val, current_indent=""):
        brackets = ("", "")
        content = []

        if isinstance(val, dict):
            brackets = ("{", "}")
            for k in sorted(val) if sort_keys else val.keys():
                if invalid_key(k): continue
                v = val[k]
                content.append(encoder(repr(k), v, current_indent + indent))
        elif isinstance(val, list):
            brackets = ("[", "]")
            for item in val:
                content.append(encoder(None, item, current_indent + indent))
        else:
            content.append(repr(val))

        return (
            current_indent +
            ("" if key is None else f"{key}{separators[1]}") +
            brackets[0] +
            (newline if content and brackets[0] else "") +
            f"{separators[0]}{newline}".join(content) +
            (f"{newline}{current_indent}" if content and brackets[0] else "") +
            brackets[1]
        )

    return encoder(None, obj)