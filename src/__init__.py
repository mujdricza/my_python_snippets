import os

# I prefer using os.path instead of pathlib.Path
PROJECT_ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(PROJECT_ROOT_DIR, "data")

# importing environment variable if set
SPEC_DATA_DIR = os.getenv("DATA_DIR", DATA_DIR)

"""
# alternatives with pathlib and importlib
from pathlib import Path
from importlib.resources import files

PROJECT_ROOT_DIR = Path(__file__).resolve().parents[2]
SPEC_DATA_DIR = str(files("data"))  # NOTE files() searches recursively - can be ambiguous
"""
