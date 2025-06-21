"""Simple interpreter orchestrating lexer, parser, and evaluator."""

from __future__ import annotations

from typing import Any, Dict, List, Callable

from .parser import Parser
from .borrow_checker import BorrowChecker
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


class Interpreter:
    def __init__(self) -> None:
        self.borrow_checker = BorrowChecker()
        self.env: Dict[str, Any] = {}
        self.builtins: Dict[str, Callable[..., Any]] = {
            "add": lambda a, b: a + b,
            "sub": lambda a, b: a - b,
            "mul": lambda a, b: a * b,
            "div": lambda a, b: a / b,
            "sum": lambda arr: sum(arr),
            "print": print,
        }

    def eval(self, source: str) -> List[Any]:
        parser = Parser(source)
        exprs = parser.parse()
        # Borrow check (no-op placeholder)
        self.borrow_checker.check(exprs)
        results: List[Any] = []
        for expr in exprs:
            results.append(self.eval_expr(expr))
        return results

    def eval_expr(self, expr: Expr) -> Any:
        if isinstance(expr, Number):
            return expr.value
        if isinstance(expr, StringLiteral):
            return expr.value
        if isinstance(expr, Boolean):
            return expr.value
        if isinstance(expr, Identifier):
            if expr.name in self.env:
                return self.env[expr.name]
            raise NameError(expr.name)
        if isinstance(expr, ArrayExpr):
            return [self.eval_expr(e) for e in expr.elements]
        if isinstance(expr, Assignment):
            value = self.eval_expr(expr.value)
            self.env[expr.target.name] = value
            return value

        if isinstance(expr, BinaryOp):
            left = self.eval_expr(expr.left)
            right = self.eval_expr(expr.right)
            if expr.op == '+':
                return left + right
            if expr.op == '-':
                return left - right
            if expr.op == '*':
                return left * right
            if expr.op == '/':
                return left / right
            if expr.op == '==':
                return left == right
            if expr.op == '!=':
                return left != right
            if expr.op == '<':
                return left < right
            if expr.op == '>':
                return left > right
            if expr.op == '<=':
                return left <= right
            if expr.op == '>=':
                return left >= right
            raise ValueError(f"Unknown operator {expr.op}")
        if isinstance(expr, IfExpr):
            cond = self.eval_expr(expr.cond)
            return self.eval_expr(expr.then_branch if cond else expr.else_branch)
        if isinstance(expr, Call):
            func_name = expr.func.name
            args = [self.eval_expr(a) for a in expr.args]
            if func_name in self.builtins:
                return self.builtins[func_name](*args)
            raise NameError(f"Unknown function {func_name}")
        raise TypeError(f"Unhandled expression type {type(expr)}")

