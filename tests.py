import ast

testobj = {
    'lorem': 'ipsum',
    'one': {},
    'two': [],
    'three': [
        {
            'test': False,
            'test': {
                'foo': 'bar',
                'baz': 0
            }
        }
    ],
    # Ellipsis: 'ellipsis',
    # 'ellipsis': Ellipsis,

    # (1, 2, 3): 'tuple',
    # range(10): 'range',
    # frozenset({1, 2, 3}): 'frozenset'
}

# testobj['self'] = testobj

formatted = pretty_repr(testobj, indent=4)

try:
    passed = ast.literal_eval(formatted) == testobj
except SyntaxError:
    passed = False
assert passed