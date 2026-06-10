"""
We discussed the best practice recommendation to avoid f""-style format-strings
in logs.

See e.g.
- https://christopher.xyz/2019/02/07/python-logging-interpolation.html
- https://betterstack.com/community/guides/logging/python/python-logging-best-practices/
- https://discuss.python.org/t/safer-logging-methods-for-f-strings-and-new-style-formatting/13802

The below code is experimenting with these information.

Further related information
- https://coralogix.com/blog/python-logging-best-practices-tips/
"""


import logging

def christopher_exp1():
    username = 'jdoe'
    logging.info(f"{username} logged in")         # (1) bad
    logging.info("{} logged in".format(username)) # (2) bad
    logging.info("%s logged in" % username)       # (3) bad
    logging.info("%s logged in", username)        # (4) good

    # record: logging.LogRecord...

    #  class logging.LogRecord(name, level, pathname, lineno, msg, args, exc_info, func=None, sinfo=None)
    record1 = logging.LogRecord(name="root", level=logging.INFO, pathname=__file__, lineno=18,
                                msg=f"{username} logged in", args=username, exc_info=None)
    record2 = logging.LogRecord(name="root", level=logging.INFO, pathname=__file__, lineno=19,
                                msg="{} logged in", args=(username), exc_info=None)
    record3 = logging.LogRecord(name="root", level=logging.INFO, pathname=__file__, lineno=20,
                                msg="%s logged in", args=(username), exc_info=None)
    # TODO how to make record4 different from record3 ? (different formatting style)
    record4 = logging.LogRecord(name="root", level=logging.INFO, pathname=__file__, lineno=21,
                                msg="%s logged in", args=(username), exc_info=None)
    records = [record1, record2, record3, record4]
    for record in records:
        print(f"record.msg = '{record.msg}', record.args = '{record.args}'")

    # christopher's outputs:
    # # record attributes for our log messages
    # record.msg, record.args == "jdoe logged in", ()  # (1)
    # record.msg, record.args == "jdoe logged in", ()  # (2)
    # record.msg, record.args == "jode logged in", ()  # (3)
    # record.msg, record.args == "%s logged in", ("jdoe",)  # (4)

    # my outputs
    # record.msg = 'jdoe logged in', record.args = 'jdoe'
    # record.msg = '{} logged in', record.args = 'jdoe'
    # record.msg = '%s logged in', record.args = 'jdoe'
    # record.msg = '%s logged in', record.args = 'jdoe'


def discuss_python_exp1():
    logger = logging.getLogger("discuss_logger")
    logger.setLevel(logging.INFO)
    untrusted_string = "untrusted ${name}"  # How to fill this string to make it dangerous?
    some_dict = {}  # How to fill this dict to make it dangerous?
    logger.info('look: %s', untrusted_string)  # OK
    logger.info('look: %(foo)s', {'foo', untrusted_string})  # OK
    logger.info(f'look: {untrusted_string}')  # OK
    logger.info(f'look: {untrusted_string}', some_dict)  # DANGER!


"""Here, we see that calling a function within logging can affect the
    results, even if the logging function is not active!
"""
# Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
# -- same with Python 3.11.7 (main, Dec  8 2023, 18:56:58) [GCC 11.4.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import logging
# >>> logger = logging.getLogger("l")
# >>> def fct():
# ...   return "fct-return"
# ...
# >>> name = "My Name"
# >>> def fct():
# ...   global name
# ...   name = "fct-name"
# ...   return "fct-return"
# ...
# >>> logger.warning(f"fct: {fct()}, name: {name}")
# fct: fct-return, name: fct-name
# >>> name
# 'fct-name'
# >>> name = "My Name"
# >>> name
# 'My Name'
# >>> logger.debug(f"fct: {fct()}, name: {name}")
# >>> name
# 'fct-name'


def discuss_python_gregory_p_exp1():
    """I cannot reproduce the interactive side-effect in functions."""

    name = "My Name"

    def fct():
        global name  # it is not typical to import globals into a function, but possible
        name = "fct-name"
        return "fct-return"

    logger = logging.getLogger("gregory_p_logger")
    logger.setLevel(logging.INFO)
    print(logger)

    logger.warning(f"My name is first: {name}")
    #logger.info("The function's result is '%s', and my name is: '%s'", fct(), name)
    logger.warning(f"The function's result is '{fct()}', and my name is: '{name}'")
    logger.warning(f"My name is again: {name}")


if __name__ == "__main__":
    # christopher_exp1()
    # discuss_python_exp1()
    discuss_python_gregory_p_exp1()