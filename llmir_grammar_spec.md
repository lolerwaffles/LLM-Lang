**LLM-IR Grammar Specification (Draft)**

```
Program         ::= Module*
Module          ::= Identifier ← $import StringLiteral | FunctionDef | ConstantDef

FunctionDef     ::= Identifier ← ParamList Block
ParamList       ::= Identifier*
Block           ::= Expression | (Expression ';')*

Expression      ::= Literal
                 | Identifier
                 | FunctionCall
                 | Assignment
                 | BinaryOp
                 | UnaryOp
                 | ArrayExpr
                 | IfExpr

FunctionCall    ::= Identifier '(' ArgList ')'
ArgList         ::= Expression*

Assignment      ::= Identifier ← Expression
BinaryOp        ::= Expression Operator Expression
UnaryOp         ::= Operator Expression
ArrayExpr       ::= '[' Expression* ']'
IfExpr          ::= 'if' Expression 'then' Expression 'else' Expression

Operator        ::= '+' | '-' | '*' | '/' | '^' | '%' | '==' | '!=' | '<' | '>' | '<=' | '>='

Literal         ::= Number | StringLiteral | Boolean
Number          ::= [0-9]+(\.[0-9]+)?
Boolean         ::= 'true' | 'false'
StringLiteral   ::= '"' .*? '"'

Identifier      ::= [a-zA-Z_][a-zA-Z0-9_]*
```

This grammar is expression-based, supporting nested logic and compact syntax for token efficiency. All blocks are expressions and return values.

