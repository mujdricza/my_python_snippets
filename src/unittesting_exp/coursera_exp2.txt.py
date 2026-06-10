import unittest

class TestExample(unittest.TestCase):
    def test_assertion(self):
        self.assertEquals("some string", "some")


"""
class TestProgram(builtins.object)
 |  TestProgram(module='__main__', defaultTest=None, argv=None, testRunner=None, testLoader=<unittest.loader.TestLoader object at 0x7fc483929cc0>, exit=True, verbosity=1, failfast=None, catchbreak=None, buffer=None, warnings=None, *, tb_locals=False)
 |
 |  A command-line program that runs a set of tests; this is primarily
 |  for making test modules conveniently executable.
 |
 |  Methods defined here:
 |
 |  __init__(self, module='__main__', defaultTest=None, argv=None, testRunner=None, testLoader=<unittest.loader.TestLoader object at 0x7fc483929cc0>, exit=True, verbosity=1, failfast=None, catchbreak=None, buffer=None, warnings=None, *, tb_locals=False)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  createTests(self, from_discovery=False, Loader=None)
 |
 |  parseArgs(self, argv)
 |
 |  runTests(self)
 |
 |  usageExit(self, msg=None)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  buffer = None
 |
 |  catchbreak = None
 |
 |  failfast = None
 |
 |  module = None
 |
 |  progName = None
 |
 |  testNamePatterns = None
 |
 |  verbosity = 1
 |
 |  warnings = None
 """
unittest.main(argv=[""], verbosity=2, exit=False)