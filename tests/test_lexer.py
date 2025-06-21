import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from llmir.lexer import Lexer
from llmir.token import TokenType


class TestLexer(unittest.TestCase):
    def test_numbers_and_identifiers(self):
        lex = Lexer("foo 123")
        tokens = lex.tokenize()
        self.assertEqual(tokens[0].type, TokenType.IDENT)
        self.assertEqual(tokens[0].value, "foo")
        self.assertEqual(tokens[1].type, TokenType.NUMBER)
        self.assertEqual(tokens[1].value, "123")
        self.assertEqual(tokens[-1].type, TokenType.EOF)

    def test_strings_and_booleans(self):
        lex = Lexer('"hi" true false')
        tokens = lex.tokenize()
        self.assertEqual(tokens[0].type, TokenType.STRING)
        self.assertEqual(tokens[0].value, "hi")
        self.assertEqual(tokens[1].type, TokenType.BOOLEAN)
        self.assertEqual(tokens[1].value, "true")
        self.assertEqual(tokens[2].type, TokenType.BOOLEAN)
        self.assertEqual(tokens[2].value, "false")



if __name__ == "__main__":
    unittest.main()
