import argparse
import os

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str)  # no default

    return parser.parse_args()


def get_abspath(param: str | None, default: str | None = None) -> str | None:

    if param is not None:
        return os.path.abspath(param)
    return default


if __name__ == "__main__":
    args = get_args()
    print(args)

    print(type(args.input))
    print(args.input)
    # path = os.path.abspath(args.input) if args.input else None
    path = get_abspath(args.input)
    print(path)
