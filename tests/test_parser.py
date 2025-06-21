import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from llmir.parser import Parser
from llmir.ast import ArrayExpr, Assignment, BinaryOp, Boolean, IfExpr, Number



class TestParser(unittest.TestCase):
    def test_simple_expression(self):
        parser = Parser("1+2")
        exprs = parser.parse()
        self.assertEqual(len(exprs), 1)
        expr = exprs[0]
        self.assertIsInstance(expr, BinaryOp)
        self.assertIsInstance(expr.left, Number)
        self.assertEqual(expr.left.value, 1.0)
        self.assertIsInstance(expr.right, Number)
        self.assertEqual(expr.right.value, 2.0)
        self.assertEqual(expr.op, "+")

    def test_if_and_array(self):
        parser = Parser("if true then [1,2] else [3]")
        exprs = parser.parse()
        self.assertEqual(len(exprs), 1)
        expr = exprs[0]
        self.assertIsInstance(expr, IfExpr)
        self.assertIsInstance(expr.cond, Boolean)
        self.assertTrue(expr.cond.value)
        self.assertIsInstance(expr.then_branch, ArrayExpr)
        self.assertEqual(len(expr.then_branch.elements), 2)
        self.assertIsInstance(expr.else_branch, ArrayExpr)
        self.assertEqual(len(expr.else_branch.elements), 1)



if __name__ == "__main__":
    unittest.main()
