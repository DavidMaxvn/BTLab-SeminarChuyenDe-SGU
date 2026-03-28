import numpy as np
import pandas as pd


def get_manhattan_distance(
    df1: pd.DataFrame,
    df2: pd.DataFrame,
) -> np.float64:
    """
    Tính Manhattan distance (L1 norm) giữa hai DataFrame cùng kích thước.
    """
    if not isinstance(df1, pd.DataFrame) or not isinstance(df2, pd.DataFrame):
        raise TypeError("df1 và df2 phải là pandas.DataFrame")

    if df1.shape != df2.shape:
        raise ValueError("df1 và df2 phải cùng shape.")

    if list(df1.columns) != list(df2.columns) or list(df1.index) != list(df2.index):
        raise ValueError("df1 và df2 phải cùng index và columns.")

    try:
        df1_num = df1.astype(float)
        df2_num = df2.astype(float)
    except ValueError as err:
        raise ValueError("Giá trị trong DataFrame phải có thể chuyển thành số") from err

    element_wise_dist: pd.DataFrame = (df1_num - df2_num).abs()
    dist: np.float64 = np.array(element_wise_dist).sum().astype(float)
    return np.float64(dist)