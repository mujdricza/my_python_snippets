"""
https://refactoring.guru/replace-temp-with-query


Problem
You place the result of an expression in a local variable for later use in your code.

Solution
Move the entire expression to a separate method and return the result from it. Query the method instead of using a variable. Incorporate the new method in other methods, if necessary.

EMM: ?? Why it is better to call the method x times (v2)?
- calling the method x times adds to the latency, see timing outputs below!
-> but caching (v3) does help, however, it does not beat the v1 computation

"""

from src.misc.timing import timing
from functools import cache


# not recommended
def calculateTotal_v1(quantity, itemPrice):
    basePrice = quantity * itemPrice
    if basePrice > 1000:
        return basePrice * 0.95
    else:
        return basePrice * 0.98


# recommended, but with higher latency
def calculateTotal_v2(quantity, itemPrice):
    if basePrice(quantity, itemPrice) > 1000:
        return basePrice(quantity, itemPrice) * 0.95
    else:
        return basePrice(quantity, itemPrice) * 0.98

def basePrice(quantity, itemPrice):
    return quantity * itemPrice


# recommended with caching helps to lower the latency -- NOTE that we cache the calling function where the results are created (not basePrice_cached() itself)
@cache
def calculateTotal_v3(quantity, itemPrice):
    if basePrice_cached(quantity, itemPrice) > 1000:
        return basePrice_cached(quantity, itemPrice) * 0.95
    else:
        return basePrice_cached(quantity, itemPrice) * 0.98

def basePrice_cached(quantity, itemPrice):
    return quantity * itemPrice



@timing
def main_v1(n):
    quantity = 0.5
    itemPrice = 135.2
    for i in range(n):
        calculateTotal_v1(quantity, itemPrice)


@timing
def main_v2(n):
    quantity = 0.5
    itemPrice = 135.2
    for i in range(n):
        calculateTotal_v2(quantity, itemPrice)


@timing
def main_v3(n):
    quantity = 0.5
    itemPrice = 135.2
    for i in range(n):
        calculateTotal_v3(quantity, itemPrice)


if __name__ == '__main__':
    n = 1000000
    main_v1(n)
    main_v2(n)
    main_v3(n)
    """
    1769170957490554202
    00d:00h:00m:00s:126ms
    1769170957716575298
    00d:00h:00m:00s:225ms
    1769170957869890772
    00d:00h:00m:00s:153ms
    """