from dataclasses import dataclass
from typing import List, Optional


class Expr:
    pass


@dataclass
class Number(Expr):
    value: str


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
class StringLiteral(Expr):
    value: str

