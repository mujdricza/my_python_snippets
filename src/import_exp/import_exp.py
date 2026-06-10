
from importlib import import_module

try:
    loaded_module = import_module("non-existing-name")
    # loaded_module = import_module(None)  # NOTE: None throws an AttributeError ('NoneType' object has no attribute 'startswith' due to File "/home/emm/anaconda3/envs/venv_misc-p313/lib/python3.13/importlib/__init__.py", line 80, in import_module)
except ModuleNotFoundError as e:  # ModuleNotFoundError is a kind of ImportError
    print("module not found", e)
except ImportError as e:
    print("import error", e)


    