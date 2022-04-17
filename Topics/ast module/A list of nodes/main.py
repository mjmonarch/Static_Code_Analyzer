import ast

expression = "(34 + 6) * (23**2 - 7 + 45**2)"

tree = ast.parse(expression)

node_list = []
for node in ast.walk(tree):
    node_list.append(node)
print(len(node_list))
