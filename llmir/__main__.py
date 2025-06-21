import sys
from .interpreter import Interpreter


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python -m llmir <file.llang>")
        sys.exit(1)
    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        source = f.read()
    interp = Interpreter()
    results = interp.eval(source)
    for r in results:
        if r is not None:
            print(r)


if __name__ == "__main__":
    main()
