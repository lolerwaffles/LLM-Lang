from __future__ import annotations

from typing import Any, List

from .ast import BinaryOp, Call, Expr, Identifier, Number, StringLiteral


class Interpreter:
    """Very small interpreter for demonstration purposes."""

    def eval(self, exprs: List[Expr]) -> Any:
        result: Any = None
        for expr in exprs:
            result = self.eval_expr(expr)
        return result

    def eval_expr(self, expr: Expr) -> Any:
        if isinstance(expr, Number):
            return int(expr.value)
        if isinstance(expr, StringLiteral):
            return expr.value
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
                return left // right
            raise NotImplementedError(f"Operator {expr.op}")
        if isinstance(expr, Call):
            func_name = expr.func.name
            args = [self.eval_expr(arg) for arg in expr.args]
            if func_name == 'print':
                print(*args)
                return None
            raise NotImplementedError(f"Unknown function {func_name}")
        if isinstance(expr, Identifier):
            raise NotImplementedError("Variables not supported")
        raise NotImplementedError(f"Unknown expression {expr}")
