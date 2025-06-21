from __future__ import annotations

import os
from typing import List

from .parser import Parser
from .ast import Expr


class ModuleLoader:
    """Load llmir modules from disk."""

    def load_module(self, path: str) -> List[Expr]:
        with open(path, "r", encoding="utf-8") as f:
            source = f.read()
        parser = Parser(source)
        return parser.parse()
