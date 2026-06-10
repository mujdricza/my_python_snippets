# Unittesting

The main material is based on the Coursera course https://www.coursera.org/learn/python-mlops-duke

# Info general

test fixture
    A test fixture represents the preparation needed to perform one or more tests, and any associated cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.
test case
    A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs. unittest provides a base class, TestCase, which may be used to create new test cases.
test suite
    A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.
test runner
    A test runner is a component which orchestrates the execution of tests and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.


Plain Asserts - Basic assertion statements in Python used to verify values and results.

Test Classes - Classes that contain multiple related test methods and setup/teardown logic.

Parametrize - Pytest decorator to run a test multiple times with different arguments.

Setup Method - Code that runs before each test method in a Test Class.

Teardown Method - Code that runs after each test method in a Test Class.


Test Failure Output - Pytest results containing details on which tests failed and why.

PDB (Python Debugger) - Tool to debug Python code by stepping through execution.

Pytest Fixtures - Shared test data/state managed by Pytest.

Pytest Plugins - Extensions that provide added Pytest functionality.

Pytest Options - Command line flags that control Pytest test runner behavior.

---

# Info unittest

https://docs.python.org/3/library/unittest.html



## Assertion list

https://docs.python.org/3/library/unittest.html#assert-methods

the most commonly used methods (see the tables below for more assert methods): 

| Method                    |Checks that |
|---------------------------| --- |
| assertEqual(a, b)         |a == b |
| assertNotEqual(a, b)      |a != b |
| assertTrue(x)             |bool(x) is True |
| assertFalse(x)            |bool(x) is False |
| assertIs(a, b)            |a is b |
| assertIsNot(a, b)         |a is not b |
| assertIsNone(x)           |x is None |
| assertIsNotNone(x)        |x is not None |
| assertIn(a, b)            |a in b |
| assertNotIn(a, b)         |a not in b |
| assertIsInstance(a, b)    |isinstance(a, b) |
| assertNotIsInstance(a, b) |not isinstance(a, b) |

All the assert methods accept a msg argument that, if specified, is used as the error message on failure (see also longMessage). Note that the msg keyword argument can be passed to assertRaises(), assertRaisesRegex(), assertWarns(), assertWarnsRegex() only when they are used as a context manager. 

>>> dir(unittest.TestCase)

| all methods |  |
| --- | --- |
|addClassCleanup() |  |
|  addCleanup() |  |
|  addTypeEqualityFunc() |  |
|  assertAlmostEqual() |  |
|  assertAlmostEquals() |  |
|  assertCountEqual() |  |
|  assertDictContainsSubset() |  |
|  assertDictEqual() |  |
|  assertEqual() |  |
|  assertEquals() |  |
|  assertFalse() |  |
|  assertGreater() |  |
|  assertGreaterEqual() |  |
|  assertIn() |  |
|  assertIs() |  |
|  assertIsInstance() |  |
|  assertIsNone() |  |
|  assertIsNot() |  |
|  assertIsNotNone() |  |
|  assertLess() |  |
|  assertLessEqual() |  |
|  assertListEqual() |  |
|  assertLogs() |  |
|  assertMultiLineEqual() |  |
|  assertNoLogs() |  |
|  assertNotAlmostEqual() |  |
|  assertNotAlmostEquals() |  |
|  assertNotEqual() |  |
|  assertNotEquals() |  |
|  assertNotIn() |  |
|  assertNotIsInstance() |  |
|  assertNotRegex() |  |
|  assertNotRegexpMatches() |  |
|  assertRaises() |  |
|  assertRaisesRegex() |  |
|  assertRaisesRegexp() |  |
|  assertRegex() |  |
|  assertRegexpMatches() |  |
|  assertSequenceEqual() |  |
|  assertSetEqual() |  |
|  assertTrue() |  |
|  assertTupleEqual() |  |
|  assertWarns() |  |
|  assertWarnsRegex() |  |
|  assert_() |  |
|  countTestCases() |  |
|  debug() |  |
|  defaultTestResult() |  |
|  doClassCleanups() |  |
|  doCleanups() |  |
|  fail() |  |
|  failIf() |  |
|  failIfAlmostEqual() |  |
|  failIfEqual() |  |
|  failUnless() |  |
|  failUnlessAlmostEqual() |  |
|  failUnlessEqual() |  |
|  failUnlessRaises() |  |
|  failureException() |  |
|  id() |  |
|  longMessage() |  |
|  maxDiff() |  |
|  run() |  |
|  setUp() |  |
|  setUpClass() |  |
|  shortDescription() |  |
|  skipTest() |  |
|  subTest() |  |
|  tearDown() |  |
|  tearDownClass() |  |


* `self.assertEqual(a, b)`
* `self.assertNotEqual(a, b)`
* `self.assertTrue(x)`
* `self.assertFalse(x)`
* `self.assertIs(a, b)`
* `self.assertIsNot(a, b)`
* `self.assertIsNone(x)`
* `self.assertIsNotNone(x)`
* `self.assertIn(a, b)`
* `self.assertNotIn(a, b)`
* `self.assertIsInstance(a, b)`
* `self.assertNotIsInstance(a, b)`
* `self.assertRaises(exc, fun, *args, **kwds)`
* `self.assertRaisesRegex(exc, r, fun, *args, **kwds)`
* `self.assertWarns(warn, fun, *args, **kwds)`
* `self.assertWarnsRegex(warn, r, fun, *args, **kwds)`
* `self.assertLogs(logger, level)`
* `self.assertMultiLineEqual(a, b)`
* `self.assertSequenceEqual(a, b)`
* `self.assertListEqual(a, b)`
* `self.assertTupleEqual(a, b)`
* `self.assertSetEqual(a, b)`
* `self.assertDictEqual(a, b)`
* `self.assertAlmostEqual(a, b)`
* `self.assertNotAlmostEqual(a, b)`
* `self.assertGreater(a, b)`
* `self.assertGreaterEqual(a, b)`
* `self.assertLess(a, b)`
* `self.assertLessEqual(a, b)`
* `self.assertRegex(s, r)`
* `self.assertNotRegex(s, r)`
* `self.assertCountEqual(a, b)`

  # Info pytest

https://docs.pytest.org/en/8.0.x/

- simpler
- e.g. no need of class, no need of inheritance in test classes

- test files and functions need to be prefixes with `test_`
- test classes need to be prefixed with `Test`

- install
    * `pip install pytest`

- use
  - `pytest`
  - `pytest my_project`
  - `pytest -vvv test_util.py`

- prints are possible and really printed 

---

# Related pages

https://wiki.python.org/moin/PythonTestingToolsTaxonomy
