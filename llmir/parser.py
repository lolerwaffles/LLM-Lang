from __future__ import annotations

from typing import List

from .ast import (
    ArrayExpr,
    Assignment,
    BinaryOp,
    Boolean,
    Call,
    Expr,
    Identifier,
    IfExpr,
    Number,
    StringLiteral,
)
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
        return Number(float(tok.value))

    def parse_string(self) -> StringLiteral:
        tok = self.consume()
        assert tok.type == TokenType.STRING
        return StringLiteral(tok.value)

    def parse_boolean(self) -> Boolean:
        tok = self.consume()
        assert tok.type == TokenType.BOOLEAN
        return Boolean(tok.value == "true")

    def parse_identifier(self) -> Identifier:
        tok = self.consume()
        assert tok.type == TokenType.IDENT
        return Identifier(tok.value)

    def parse_array(self) -> ArrayExpr:
        self.consume()  # [
        elements: List[Expr] = []
        while self.peek().type != TokenType.RBRACKET:
            elements.append(self.parse_expression())
            if self.peek().type == TokenType.COMMA:
                self.consume()
        self.consume()  # ]
        return ArrayExpr(elements)

    def parse_call(self, ident: Identifier) -> Call:
        self.consume()  # (
        args: List[Expr] = []
        while self.peek().type != TokenType.RPAREN:
            args.append(self.parse_expression())
            if self.peek().type == TokenType.COMMA:
                self.consume()
        self.consume()
        return Call(ident, args)

    def parse_if_expr(self) -> IfExpr:
        self.consume()  # if
        cond = self.parse_expression()
        self.consume()  # then
        then_branch = self.parse_expression()
        self.consume()  # else
        else_branch = self.parse_expression()
        return IfExpr(cond, then_branch, else_branch)

    def parse_primary(self) -> Expr:
        tok = self.peek()
        if tok.type == TokenType.NUMBER:
            return self.parse_number()
        if tok.type == TokenType.STRING:
            return self.parse_string()
        if tok.type == TokenType.BOOLEAN:
            return self.parse_boolean()
        if tok.type == TokenType.IDENT:
            ident = self.parse_identifier()
            if self.peek().type == TokenType.LPAREN:
                return self.parse_call(ident)
            return ident
        if tok.type == TokenType.LBRACKET:
            return self.parse_array()
        if tok.type == TokenType.LPAREN:
            self.consume()
            expr = self.parse_expression()
            self.consume()  # RPAREN
            return expr
        if tok.type == TokenType.IF:
            return self.parse_if_expr()
        raise SyntaxError(f"Unexpected token {tok}")

    def parse_expression(self) -> Expr:
        expr = self.parse_primary()
        if isinstance(expr, Identifier) and self.peek().type == TokenType.ASSIGN:
            self.consume()
            value = self.parse_expression()
            return Assignment(expr, value)
        while self.peek().type == TokenType.OPERATOR:
            op = self.consume().value
            right = self.parse_primary()
            expr = BinaryOp(expr, op, right)
        return expr

    def parse(self) -> List[Expr]:
        exprs: List[Expr] = []
        while self.peek().type != TokenType.EOF:
            exprs.append(self.parse_expression())
        return exprs
