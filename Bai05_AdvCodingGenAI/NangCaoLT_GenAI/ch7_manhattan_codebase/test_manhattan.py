import pandas as pd
import pytest
from src.manhattan import get_manhattan_distance


def test_basic_manhattan_distance():
    df1 = pd.DataFrame(
        data=[[1, 3], [2, 4]],
        index=["a", "b"],
        columns=["A", "B"],
    )

    df2 = pd.DataFrame(
        data=[[5, 7], [6, 8]],
        index=["a", "b"],
        columns=["A", "B"],
    )

    assert get_manhattan_distance(df1, df2) == pytest.approx(16.0)


def test_shape_mismatch_raises():
    df1 = pd.DataFrame([[1, 2], [3, 4]])
    df2 = pd.DataFrame([[1, 2, 3]])

    with pytest.raises(ValueError):
        get_manhattan_distance(df1, df2)


def test_index_columns_mismatch_raises():
    df1 = pd.DataFrame([[1, 2], [3, 4]], index=["a", "b"], columns=["A", "B"])
    df2 = pd.DataFrame([[1, 2], [3, 4]], index=["x", "y"], columns=["A", "B"])

    with pytest.raises(ValueError):
        get_manhattan_distance(df1, df2)


def test_non_numeric_raises():
    df1 = pd.DataFrame([["x", 2], [3, 4]])
    df2 = pd.DataFrame([[1, 2], [3, 4]])

    with pytest.raises(ValueError):
        get_manhattan_distance(df1, df2)


if __name__ == "__main__":
    pytest.main(["-q"])
