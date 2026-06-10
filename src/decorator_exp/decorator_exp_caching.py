"""
Simple solution for caching with decorator.

Source of idea see:
https://www.youtube.com/watch?v=JgxCY-tbWHA
"""

import functools

# caching for computed partial results -> lower latency
@functools.cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    print(fibonacci(10))
