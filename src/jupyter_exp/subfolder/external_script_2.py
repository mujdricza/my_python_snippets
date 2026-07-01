"""
Small script for demonstrating script usage from within Jupyter notebook
with access to a script not in the same directory as the notebook is.
"""
import sys

def leaving(name: str) -> None:
    print(f"Goodbye, {name}!")


if __name__ == "__main__":
    name = "Anonymous"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    leaving(name)
