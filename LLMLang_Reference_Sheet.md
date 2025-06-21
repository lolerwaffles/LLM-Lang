# LLMLang Primer

This sheet introduces **LLMLang** (sometimes referred to as LLM‑IR). It contains the essential schema and grammar rules so a language model can generate LLMLang code without referencing any external repository.

## 1. Language Overview

LLMLang is an expression‑oriented language that compiles to LLVM IR. The design goals are:

- **Token Efficiency** – tersely symbolic syntax for minimal token usage
- **Logic Density** – every line is an expression and returns a value
- **Execution Efficiency** – LLVM IR backend
- **Memory Safety** – ownership/borrowing rules
- **Concurrency** – actor and shared‑memory primitives
- **Interoperability** – FFI hooks for C/C++/Rust

A minimal interpreter evaluates sequences of expressions, enforcing a stub borrow checker and providing basic runtime functionality.

## 2. Tokens and Literals

- **Numbers** – digits with optional decimal point (e.g. `123` or `3.14`)
- **Strings** – text wrapped in double quotes (e.g. `"hello"`)
- **Booleans** – `true` or `false`
- **Identifiers** – start with a letter or underscore and may contain digits
- **Operators** – arithmetic and comparison symbols (`+ - * / ^ % == != < > <= >=`)
- **Brackets** – `[` `]` for arrays and `(` `)` for function calls
- **Assignment** – the left‑arrow `←`
- **Keywords** – `if`, `then`, `else`

Whitespace is insignificant outside of tokens.

## 3. Grammar

The core grammar is expression based:

```
Program       ::= Expression*
Expression    ::= Literal
                | Identifier
                | Assignment
                | BinaryOp
                | ArrayExpr
                | IfExpr
                | FunctionCall
Assignment    ::= Identifier "←" Expression
BinaryOp      ::= Expression Operator Expression
ArrayExpr     ::= '[' Expression (',' Expression)* ']'
IfExpr        ::= 'if' Expression 'then' Expression 'else' Expression
FunctionCall  ::= Identifier '(' Expression (',' Expression)* ')'
Operator      ::= '+' | '-' | '*' | '/' | '^' | '%' | '==' | '!=' | '<' | '>' | '<=' | '>='
Literal       ::= Number | StringLiteral | Boolean
Number        ::= [0-9]+(\.[0-9]+)?
Boolean       ::= 'true' | 'false'
StringLiteral ::= '"' .*? '"'
Identifier    ::= [a-zA-Z_][a-zA-Z0-9_]*
```

All expressions evaluate to a value. Assignments store values in the interpreter environment. Arrays are literal lists of expressions. Function calls may invoke built‑ins or user functions when available.

## 4. Built‑in Functions

The interpreter provides several built‑ins:

- `add(a, b)` – addition
- `sub(a, b)` – subtraction
- `mul(a, b)` – multiplication
- `div(a, b)` – division
- `sum(array)` – sum of array elements
- `print(value)` – output to console

## 5. Execution Pipeline

1. **Lexer** – tokenizes source text
2. **Parser** – converts tokens to an AST
3. **Borrow Checker** – validates ownership rules (stub)
4. **Interpreter/Compiler** – evaluates expressions or emits LLVM IR
5. **Scheduler/Runtime** – placeholders for concurrency and runtime features

## 6. Example Program

```
print("Hello, world!")

x ← 10
y ← 20
add(x, y)
mul(x, y)

nums ← [1, 2, 3, 4, 5]
sum(nums)

if sum(nums) > 10 then "big" else "small"
```

## 7. Tests

Run the LLMLang test suite with `pytest -q`.

---
This primer stands alone so an LLM can generate valid LLMLang code.
