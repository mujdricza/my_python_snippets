"""
Older way of installing needed dependencies.
"""
import setuptools
import pathlib


HERE: pathlib.Path = pathlib.Path(__file__).parent

with (HERE / "requirements.txt").open() as f:
    requires = f.read().splitlines()


__package__ = 'my_python_snippets'


setuptools.setup(
    name='my_python_snippets',
    version='0.0.1',
    description='utility functions for different tasks',
    author='Eva Mujdricza-Maydt',
    author_email='<todo>@<todo.com>',
    packages=setuptools.find_packages(),
    package_dir={__package__: __package__},
    install_requires=requires,
    test_suite='nose.collector',
    tests_require=['nose'],
)
