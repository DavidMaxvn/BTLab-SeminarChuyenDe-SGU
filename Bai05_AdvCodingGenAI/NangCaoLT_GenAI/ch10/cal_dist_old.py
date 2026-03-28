import math
import pandas as pd
import numpy as np


def calculate_distance_old(a, b, mode):
    if mode != "l1" and mode != "l2":
        raise ValueError("mode must be l1 or l2")

    if a.shape != b.shape:
        raise ValueError("shape mismatch")

    x = 0
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            if mode == "l1":
                x = x + abs(a.iloc[i, j] - b.iloc[i, j])
            else:
                x = x + (a.iloc[i, j] - b.iloc[i, j]) ** 2

    if mode == "l2":
        x = math.sqrt(x)

    return x