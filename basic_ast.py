import ast

node_add = ast.Expression(ast.BinOp(
                ast.Num(5),
                ast.Mult(),
                ast.Num(6)))

node_pt = ast.parse('''
favs = ['abc', 'def']
name = 'nonameinc'

for item in favs:
    print ('%s likes %s' %(name, item))
''')


class Obf_visit(ast.NodeVisitor):
    def __init__(self):
        ast.NodeVisitor.__init__(self)
    def visit_Num(self, node):
        if isinstance(node.n, int):
            print ("Numbers: %s" % str(node.n))
    def visit_Str(self, node):
        if isinstance(node.s, str):
            print ("String: %s" % node.s)


class Obf_change(ast.NodeTransformer):
    def __init__(self):
        ast.NodeTransformer.__init__(self)
    def visit_Num(self, node):
        if isinstance(node.n, int):
            return ast.Num(node.n*3)
    def visit_Str(self, node):
        if isinstance(node.s, str):
            return ast.Str(node.s[:-1])
          


Obf_v = Obf_visit()
Obf_c = Obf_change()

node_pt_fx = ast.fix_missing_locations(node_pt)
node_add_fx = ast.fix_missing_locations(node_add)

print(Obf_v.visit(node_pt_fx))
print(Obf_v.visit(node_add_fx))
print ('\n')
print(Obf_c.visit(node_pt_fx))
print(Obf_c.visit(node_add_fx))
print ('\n')
print(Obf_v.visit(node_pt_fx))
print(Obf_v.visit(node_add_fx))

