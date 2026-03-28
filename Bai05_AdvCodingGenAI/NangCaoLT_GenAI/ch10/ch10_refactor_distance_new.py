import math
import pandas as pd
import numpy as np

try:
    from ch10.cal_dist_old import calculate_distance_old
except ModuleNotFoundError:
    # fallback khi chạy trực tiếp trong thư mục ch10
    from cal_dist_old import calculate_distance_old


def get_manhattan_distance(df1: pd.DataFrame, df2: pd.DataFrame) -> float:
    """
    Compute Manhattan distance (L1 norm) between two matrices.
    """
    diff: pd.DataFrame = (df1 - df2).abs()
    distance: float = float(diff.to_numpy().sum())
    return distance


def get_euclidean_distance(df1: pd.DataFrame, df2: pd.DataFrame) -> float:
    """
    Compute Euclidean distance (L2 / Frobenius norm) between two matrices.
    """
    diff: np.ndarray = (df1 - df2).to_numpy()
    squared_sum: float = float((diff ** 2).sum())
    distance: float = math.sqrt(squared_sum)
    return distance


def calculate_distance_refactored(
    df1: pd.DataFrame,
    df2: pd.DataFrame,
    mode: str,
) -> float:
    """
    Dispatch distance calculation based on mode.
    """
    if df1.shape != df2.shape:
        raise ValueError("df1 và df2 phải cùng shape.")

    if mode == "l1":
        return get_manhattan_distance(df1, df2)
    if mode == "l2":
        return get_euclidean_distance(df1, df2)

    raise ValueError("mode phải là 'l1' hoặc 'l2'")


if __name__ == "__main__":
    df1 = pd.DataFrame([[1, 2], [3, 4]])
    df2 = pd.DataFrame([[5, 6], [7, 8]])

    print("Old L1:", calculate_distance_old(df1, df2, "l1"))
    print("New L1:", calculate_distance_refactored(df1, df2, "l1"))

    print("Old L2:", calculate_distance_old(df1, df2, "l2"))
    print("New L2:", calculate_distance_refactored(df1, df2, "l2"))