from __future__ import annotations

from typing import List

from .ast import BinaryOp, Call, Expr, Identifier, Number
from .lexer import Lexer
from .token import Token, TokenType


class Parser:
    def __init__(self, source: str) -> None:
        self.lexer = Lexer(source)
        self.tokens = self.lexer.tokenize()
        self.pos = 0

    def peek(self) -> Token:
        return self.tokens[self.pos]

    def consume(self) -> Token:
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def parse_number(self) -> Number:
        tok = self.consume()
        assert tok.type == TokenType.NUMBER
        return Number(tok.value)

    def parse_identifier(self) -> Identifier:
        tok = self.consume()
        assert tok.type == TokenType.IDENT
        return Identifier(tok.value)

    def parse_primary(self) -> Expr:
        tok = self.peek()
        if tok.type == TokenType.NUMBER:
            return self.parse_number()
        if tok.type == TokenType.IDENT:
            return self.parse_identifier()
        raise SyntaxError(f"Unexpected token {tok}")

    def parse_expression(self) -> Expr:
        left = self.parse_primary()
        while self.peek().type == TokenType.OPERATOR:
            op = self.consume().value
            right = self.parse_primary()
            left = BinaryOp(left, op, right)
        return left

    def parse(self) -> List[Expr]:
        exprs: List[Expr] = []
        while self.peek().type != TokenType.EOF:
            exprs.append(self.parse_expression())
        return exprs
