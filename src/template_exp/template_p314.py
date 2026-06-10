"""
https://www.youtube.com/watch?v=vymJMn97wks

needs Python >=3.14

- safer as f-strings
- re-usable
- after substitute() -> string like f-strings
"""
import functools

from string.templatelib import Template


def template_exp2():
    name: str = "Bobby"
    age: int = 30
    template: Template = t"Hello, {name}! You are {age} old."
    print(template.strings)
    print(template.values)
    print(template.interpolations)


# def template_exp3():


if __name__ == '__main__':

    template_exp2()
    # ('Hello, ', '! You are ', ' old.')
    # ('Bobby', 30)
    # (Interpolation('Bobby', 'name', None, ''), Interpolation(30, 'age', None, ''))

