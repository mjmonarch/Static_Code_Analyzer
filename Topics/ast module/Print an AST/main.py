import ast

code_ast = ast.parse(code)
print(ast.dump(code_ast))
