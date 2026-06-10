from functools import wraps
from time import time, time_ns, perf_counter_ns
from datetime import datetime


def timing_simple(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()

        print('func:%r args:[%r, %r] took: %2.4f sec' % (f.__name__, args, kw, te - ts))
        # print('func:%r took: %2.4f sec' % (f.__name__, te-ts))
        return result

    return wrap


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time_ns()
        result = f(*args, **kw)
        te = time_ns()
        print(te)
        time_diff_in_nanoseconds = te - ts
        time_diff_in_milliseconds = time_diff_in_nanoseconds // 1000000

        seconds, milliseconds = divmod(time_diff_in_milliseconds, 1000)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        formatted_time_diff = f"{days:>02}d:{hours:>02}h:{minutes:>02}m:{seconds:>02}s:{milliseconds:>02}ms"
        print(formatted_time_diff)
        return result

    return wrap


@timing
def myfunc(a: str, b: list, c="abc"):
    print(f"{a}, {b}, {c}")
    return a + c


if __name__ == "__main__":
    myfunc("hallo ", [1, 2, 3])
