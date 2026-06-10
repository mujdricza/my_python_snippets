"""
https://stackoverflow.com/questions/48812097/mocking-an-imported-function-with-pytest
"""
def foo(*args, **kwargs):
    """Some function that we're going to mock."""
    raise NotImplementedError()
    # return args, kwargs
