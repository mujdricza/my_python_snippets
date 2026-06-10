"""
Experimenting with Profiling

https://stackoverflow.com/questions/32926847/profiling-a-python-program-with-pycharm-or-any-other-ide
https://www.jetbrains.com/help/pycharm/profiler.html
https://www.jetbrains.com/help/pycharm/read-the-profiling-report.html

python -m cProfile -s 'calls' <your_program>.py


pip install snakeviz
Then:
python -m cProfile -o program.prof my_program.py
snakeviz program.prof

"
PyCharm allows running the current run/debug configuration while attaching a Python profiler to it. Note that the Diagrams plugin that is bundled with PyCharm should be enabled.

If you have a yappi profiler installed on your interpreter, PyCharm starts the profiling session with it by default; otherwise it uses the standard cProfile profiler.

Besides these two tracing profilers, PyCharm supports also sampling (statistical) profiler vmprof, which should be installed on the selected Python interpreter."

"""
import cProfile
import cProfile as profile
from pyinstrument import Profiler

def example_1():
    # https://stackoverflow.com/questions/32926847/profiling-a-python-program-with-pycharm-or-any-other-ide
    # In outer section of code
    pr = profile.Profile()
    pr.disable()

    # In section you want to profile
    pr.enable()
    # code of interest
    pr.disable()

    # Back in outer section of code
    pr.dump_stats('profile.pstat')


def example_2():
    import cProfile

    pr = cProfile.Profile()
    pr.enable()
    # your_function_call()
    print("Halihallo")
    pr.disable()
    # after your program ends
    pr.print_stats(sort="calls")


def example_3():
    # https://pyinstrument.readthedocs.io/en/latest/guide.html#profile-a-python-script
    pr = Profiler()
    with pr:
        print("Halihallo")
    pr.output_html()
    pr.write_html("profiling_exp-out.html")
    # pr.open_in_browser()


if __name__ == "__main__":
    example_3()

