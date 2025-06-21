from llmir.parser import Parser
from llmir.interpreter import Interpreter

code = 'print("Hello, world!")'
parser = Parser(code)
exprs = parser.parse()
Interpreter().eval(exprs)

