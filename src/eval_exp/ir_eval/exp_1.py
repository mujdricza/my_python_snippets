"""
Trying out IR related metrics of scikit-learn

Needs: pip install -U scikit-learn
"""

import numpy as np
from sklearn.metrics import (
    label_ranking_average_precision_score,
    label_ranking_loss,
    # top_k_accuracy_score,
)


def exp1():

    y_true = np.array([[1, 0, 0], [0, 0, 1]])

    #y_score = np.array([[0.75, 0.5, 1], [1, 0.2, 0.1]])
    y_score = np.array([[0.5, 0.85, 0.0], [0, 0.2, 1]])

    res = label_ranking_average_precision_score(y_true, y_score)
    print(f"label_ranking_average_precision_score: {res}")
    res = label_ranking_loss(y_true, y_score)
    print(f"label_ranking_loss: {res}")


if __name__ == "__main__":
    exp1()
