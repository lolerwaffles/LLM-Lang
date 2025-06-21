from dataclasses import dataclass
from typing import List, Optional


class Expr:
    pass


@dataclass
class Number(Expr):
    value: float


@dataclass
class StringLiteral(Expr):
    value: str


@dataclass
class Boolean(Expr):
    value: bool


@dataclass
class Identifier(Expr):
    name: str


@dataclass
class BinaryOp(Expr):
    left: Expr
    op: str
    right: Expr


@dataclass
class Call(Expr):
    func: Identifier
    args: List[Expr]

@dataclass
class ArrayExpr(Expr):
    elements: List[Expr]


@dataclass
class Assignment(Expr):
    target: Identifier
    value: Expr


@dataclass
class IfExpr(Expr):
    cond: Expr
    then_branch: Expr
    else_branch: Expr

