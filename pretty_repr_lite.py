def pretty_repr(obj, indent=4):
    def encoder(key, val, level=0):
        indent_spaces = " " * level
        brackets = ("", "")
        content = []

        if isinstance(val, dict):
            brackets = ("{", "}")
            for k, v in val.items():
                content.append(encoder(repr(k), v, level + indent))

        elif isinstance(val, list):
            brackets = ("[", "]")
            for item in val:
                content.append(encoder(None, item, level + indent))

        else:
            content.append(repr(val))

        return (
            indent_spaces +
            ("" if key is None else f"{key}: ") +
            brackets[0] +
            ("\n" if content and brackets[0] else "") +
            ",\n".join(content) +
            (f"\n{indent_spaces}" if content and brackets[0] else "") +
            brackets[1]
        )

    return encoder(None, obj)