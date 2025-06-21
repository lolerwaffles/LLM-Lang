"""Simple helper to execute the ``hello.llang`` example."""

from llmir.interpreter import Interpreter


def main() -> None:
    with open("hello.llang", "r", encoding="utf-8") as f:
        source = f.read()
    Interpreter().eval(source)


if __name__ == "__main__":
    main()

