import numpy as np


def main(res):
    weight = np.array([6, 1, 5, 1, 8], dtype=float)
    res = np.asarray(res, dtype=float)
    res = np.dot(res, weight)
    res /= np.sum(weight)
    return res
