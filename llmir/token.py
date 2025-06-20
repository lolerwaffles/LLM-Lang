from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional


class TokenType(Enum):
    NUMBER = auto()
    STRING = auto()
    IDENT = auto()
    OPERATOR = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    LPAREN = auto()
    RPAREN = auto()
    ASSIGN = auto()
    COMMA = auto()
    IF = auto()
    THEN = auto()
    ELSE = auto()
    EOF = auto()
@dataclass
class Token:
    type: TokenType
    value: Optional[str] = None
    pos: int = 0

    def __repr__(self) -> str:
        return f"Token({self.type}, {self.value})"
