import ast


tree = ast.parse(code)

fucntion_list = []
for node in ast.walk(tree):
    if isinstance(node, ast.Call):
        fucntion_list.append(node.func.id)

print(fucntion_list)