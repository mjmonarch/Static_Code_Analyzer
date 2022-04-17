import ast

tree = ast.parse(code)

for node in ast.walk(tree):
    if isinstance(node, ast.Import):
        for name in node.names:
            print(name.name)

