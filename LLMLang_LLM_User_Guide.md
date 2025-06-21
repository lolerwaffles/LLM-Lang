# LLMLang Guide for LLMs

This document summarizes how to use the minimal implementation of **LLMLang** included in this repository. It is intended to be provided to an LLM so it knows the language syntax, builtins, and overall execution flow.

## Overview

LLMLang (also referred to as *LLM-IR*) is a compact, expression-oriented language designed for efficient token usage. It compiles to LLVM IR and supports a Rust-like ownership model, arrays, conditionals, function calls, and simple concurrency primitives.

The repository includes a lexer, parser, borrow checker stub, scheduler, runtime skeleton, and a basic interpreter capable of evaluating expressions.

## Design Principles

1. **Token Efficiency** – tersely symbolic syntax.
2. **Logic Density** – expression-based structure.
3. **Execution Efficiency** – direct LLVM IR backend.
4. **Memory Safety** – Rust-style ownership/borrowing model.
5. **Concurrency** – actor and shared-memory support.
6. **Interoperability** – FFI for C/C++/Rust libraries.

See `llmir_language_design_goals.md` for the full list.

## Core Syntax

The grammar is expression-based (see `llmir_grammar_spec.md`). Key forms include:

```
Program       ::= Expression*
Expression    ::= Literal
                 | Identifier
                 | Assignment
                 | BinaryOp
                 | ArrayExpr
                 | IfExpr
                 | FunctionCall

Assignment    ::= Identifier ← Expression
BinaryOp      ::= Expression Operator Expression
ArrayExpr     ::= '[' Expression* ']'
IfExpr        ::= 'if' Expression 'then' Expression 'else' Expression
FunctionCall  ::= Identifier '(' Expression* ')'
```

Literals include numbers, strings, and booleans (`true`/`false`). Operators cover arithmetic (`+ - * /`) and comparisons (`== != < > <= >=`).

## Interpreter

The interpreter evaluates parsed AST nodes. Built‑in functions include:

- `add(a, b)` – addition
- `sub(a, b)` – subtraction
- `mul(a, b)` – multiplication
- `div(a, b)` – division
- `sum(array)` – sum of array elements
- `print(value)` – output to console

The interpreter stores variables in a simple dictionary and supports assignments and `if` expressions. Arrays are evaluated recursively.

Example usage from Python:

```python
from llmir import Interpreter

interp = Interpreter()
result = interp.eval("x ← 2 add(x, 3)")
print(result)  # -> [2, 5]
```

Each call to `eval` returns a list of the results of the top-level expressions.

## Execution Pipeline

1. **Lexer** – converts source text to tokens.
2. **Parser** – creates AST nodes from tokens.
3. **Borrow Checker** – stub that validates ownership rules (no-op).
4. **Interpreter/Compiler** – evaluate expressions or emit LLVM IR.
5. **Scheduler/Runtime** – placeholders for concurrency and runtime services.

## Extending the Language

Modules can be loaded via `$import` (lexer recognizes this token). The compiler stub illustrates how AST nodes map to LLVM IR. The scheduler and runtime are minimal and meant for experimentation.

## Running Tests

Unit tests reside under `tests/` and can be executed with `pytest -q`.

