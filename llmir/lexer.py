from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List

from .token import Token, TokenType


@dataclass
class Lexer:
    source: str

    def tokenize(self) -> List[Token]:
        tokens: List[Token] = []
        i = 0
        length = len(self.source)
        while i < length:
            ch = self.source[i]
            if ch.isspace():
                i += 1
                continue
            if ch.isdigit():
                start = i
                while i < length and self.source[i].isdigit():
                    i += 1
                tokens.append(Token(TokenType.NUMBER, self.source[start:i], start))
                continue
            if ch.isalpha() or ch == '_':
                start = i
                while i < length and (self.source[i].isalnum() or self.source[i] == '_'):
                    i += 1
                ident = self.source[start:i]
                if ident == 'if':
                    tokens.append(Token(TokenType.IF, ident, start))
                elif ident == 'then':
                    tokens.append(Token(TokenType.THEN, ident, start))
                elif ident == 'else':
                    tokens.append(Token(TokenType.ELSE, ident, start))
                else:
                    tokens.append(Token(TokenType.IDENT, ident, start))
                continue
            if ch == '(':
                tokens.append(Token(TokenType.LPAREN, ch, i))
                i += 1
                continue
            if ch == ')':
                tokens.append(Token(TokenType.RPAREN, ch, i))
                i += 1
                continue
            if ch == '[':
                tokens.append(Token(TokenType.LBRACKET, ch, i))
                i += 1
                continue
            if ch == ']':
                tokens.append(Token(TokenType.RBRACKET, ch, i))
                i += 1
                continue
            if ch == ',':
                tokens.append(Token(TokenType.COMMA, ch, i))
                i += 1
                continue
            if ch == '←':
                tokens.append(Token(TokenType.ASSIGN, ch, i))
                i += 1
                continue
            if ch in '+-*/^%<>=!':
                start = i
                i += 1
                if i < length and self.source[i] == '=':
                    op = self.source[start:i+1]
                    tokens.append(Token(TokenType.OPERATOR, op, start))
                    i += 1
                else:
                    tokens.append(Token(TokenType.OPERATOR, ch, start))
                continue
            if ch == '"':
                start = i
                i += 1
                while i < length and self.source[i] != '"':
                    i += 1
                i += 1
                tokens.append(Token(TokenType.STRING, self.source[start:i], start))
                continue
            # Unknown character
            i += 1
        tokens.append(Token(TokenType.EOF, pos=length))
        return tokens
