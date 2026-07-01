"""
Small script for demonstrating script usage from within Jupyter notebook.
"""
import sys

def greeting(name: str) -> None:
    print(f"Hello, {name}!")

if __name__ == "__main__":
    name = "Anonymous"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    greeting(name)
