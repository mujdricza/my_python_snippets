"""
Using the adjusted version of https://github.com/plurch/ir_evaluation

Showing the changes:
- also accepting string elements
- also accepting different lengths of actual and predicted lists
"""

from src.eval_exp.ir_eval.ir_evaluation_metrics import (
    mean_average_precision
)

def exp1():
    golden = [[1, 2, 3],[4, 5], [5, 6]]
    system = [[1, 22, 3],[4], [25, 6, 7]]
    k = 3

    mapk = mean_average_precision(golden, system, k)
    print(mapk)


def exp2():
    golden = [["1", "2", "3"],["4", "5"], ["5", "6"]]
    system = [["1", "22", "3"],["4"], ["25", "6", "7"]]
    k = 3

    mapk = mean_average_precision(golden, system, k)
    print(mapk)


if __name__ == "__main__":
    exp1()
    exp2()

