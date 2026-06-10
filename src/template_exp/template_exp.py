"""
https://www.youtube.com/watch?v=vymJMn97wks

needs Python >=3.14

- safer as f-strings
- re-usable
- after substitute() -> string like f-strings
"""
import functools
import sys

DO_LOAD_P314_RELATED_CODE = False
python_version = sys.version_info
print(python_version)
if python_version.major > 2 and python_version.minor > 13:
    DO_LOAD_P314_RELATED_CODE = True


# from string import Template as OldTemplate
#
# if DO_LOAD_P314_RELATED_CODE:
#     from string.templatelib import Template


def ignore_code_if_not_p314(do_load_code: bool):
    def ignore_code_if_not_p314(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if do_load_code:
                res = func(*args, **kwargs)
            else:
                print("Not loading {func.__name__}()")
            return res
        return wrapper
    return ignore_code_if_not_p314


def run_old_template():
    from .template_p313 import template_exp1

    template_exp1()


@ignore_code_if_not_p314(DO_LOAD_P314_RELATED_CODE)
def run_new_template():
    from .template_p314 import template_exp2
    template_exp2()


def main():
    run_old_template()
    run_new_template()


if __name__ == '__main__':
    main()

