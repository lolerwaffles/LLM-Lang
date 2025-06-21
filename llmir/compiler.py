"""Minimal compiler stub that converts AST to pseudo LLVM IR."""

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



class Compiler:
    def compile(self, exprs: List[Expr]) -> str:
        lines = ["; ModuleID = 'llmir'"]
        for i, expr in enumerate(exprs):
            lines.append(self.emit_expr(expr, i))
        return "\n".join(lines)

    def emit_expr(self, expr: Expr, idx: int) -> str:
        if isinstance(expr, Number):
            return f"%{idx} = add i32 0, {expr.value}"
        if isinstance(expr, Boolean):
            val = 1 if expr.value else 0
            return f"%{idx} = add i1 0, {val}"
        if isinstance(expr, StringLiteral):
            return f"; string \"{expr.value}\""

        if isinstance(expr, Identifier):
            return f"; identifier {expr.name}"
        if isinstance(expr, BinaryOp):
            left = self.emit_expr(expr.left, idx)
            right = self.emit_expr(expr.right, idx + 1)
            op_map = {'+': 'add', '-': 'sub', '*': 'mul', '/': 'sdiv'}
            op = op_map.get(expr.op, 'add')
            return f"%{idx} = {op} i32 %{idx}, %{idx + 1}"
        if isinstance(expr, Assignment):
            value = self.emit_expr(expr.value, idx)
            return value + f"\n; assign {expr.target.name}"
        if isinstance(expr, ArrayExpr):
            parts = [self.emit_expr(e, idx + i) for i, e in enumerate(expr.elements)]
            return "\n".join(parts)
        if isinstance(expr, Call):
            args = [self.emit_expr(a, idx + i) for i, a in enumerate(expr.args)]
            return "\n".join(args) + f"\n; call {expr.func.name}"
        if isinstance(expr, IfExpr):
            cond = self.emit_expr(expr.cond, idx)
            then_ir = self.emit_expr(expr.then_branch, idx + 1)
            else_ir = self.emit_expr(expr.else_branch, idx + 2)
            return "\n".join([cond, then_ir, else_ir, "; if expr"])

        return f"; unknown expr"
