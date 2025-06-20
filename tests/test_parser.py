import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from llmir.parser import Parser
from llmir.ast import BinaryOp, Identifier, Number


class TestParser(unittest.TestCase):
    def test_simple_expression(self):
        parser = Parser("1+2")
        exprs = parser.parse()
        self.assertEqual(len(exprs), 1)
        expr = exprs[0]
        self.assertIsInstance(expr, BinaryOp)
        self.assertIsInstance(expr.left, Number)
        self.assertEqual(expr.left.value, "1")
        self.assertIsInstance(expr.right, Number)
        self.assertEqual(expr.right.value, "2")
        self.assertEqual(expr.op, "+")


if __name__ == "__main__":
    unittest.main()
