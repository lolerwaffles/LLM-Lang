"""Minimal compiler stub that converts AST to pseudo LLVM IR."""

from __future__ import annotations

from typing import List

from .ast import BinaryOp, Call, Expr, Identifier, Number


class Compiler:
    def compile(self, exprs: List[Expr]) -> str:
        lines = ["; ModuleID = 'llmir'"]
        for i, expr in enumerate(exprs):
            lines.append(self.emit_expr(expr, i))
        return "\n".join(lines)

    def emit_expr(self, expr: Expr, idx: int) -> str:
        if isinstance(expr, Number):
            return f"%{idx} = add i32 0, {expr.value}"
        if isinstance(expr, Identifier):
            return f"; identifier {expr.name}"
        if isinstance(expr, BinaryOp):
            left = self.emit_expr(expr.left, idx)
            right = self.emit_expr(expr.right, idx + 1)
            op_map = {'+': 'add', '-': 'sub', '*': 'mul', '/': 'sdiv'}
            op = op_map.get(expr.op, 'add')
            return f"%{idx} = {op} i32 %{idx}, %{idx + 1}"
        return f"; unknown expr"
