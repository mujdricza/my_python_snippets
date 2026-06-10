"""`my_module` defining MyClass."""
from my_library import foo


class MyClass:
    """Some class used to demonstrate mocking imported functions."""
    def should_call_foo(self, *args, **kwargs):
        return foo(*args, **kwargs)

VAR = 0
class MyClassWithIssueInInit:
    def __init__(self, *args, **kwargs):
        self.var = foo(*args, **kwargs)

        if VAR == 0:
            raise ValueError

    def should_call_foo(self, *args, **kwargs):
        return foo(*args, **kwargs)
