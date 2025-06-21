import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from llmir.interpreter import Interpreter


class TestInterpreter(unittest.TestCase):
    def test_basic_arithmetic(self):
        interp = Interpreter()
        results = interp.eval("1+2")
        self.assertEqual(results, [3])

    def test_assignment_and_reference(self):
        interp = Interpreter()
        results = interp.eval("x ← 5 x + 1")
        self.assertEqual(results, [5, 6])

    def test_if_and_sum(self):
        interp = Interpreter()
        results = interp.eval("if false then 1 else sum([1,2,3])")
        self.assertEqual(results, [6])


if __name__ == "__main__":
    unittest.main()
