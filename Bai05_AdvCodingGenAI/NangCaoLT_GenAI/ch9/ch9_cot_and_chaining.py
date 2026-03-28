from typing import Dict
import numpy as np


def get_gross_returns(net_returns: Dict[str, float]) -> np.ndarray:
    """
    Convert net returns to gross returns by adding 1 to each value.
    """
    gross_returns: np.ndarray = np.array([1 + r for r in net_returns.values()])
    return gross_returns


def get_geometric_mean(gross_returns: np.ndarray) -> float:
    """
    Calculate geometric mean of gross returns.
    """
    if len(gross_returns) == 0:
        raise ValueError("gross_returns không được rỗng.")

    if np.any(gross_returns <= 0):
        raise ValueError("gross_returns phải > 0 để tính geometric mean.")

    product: float = float(np.prod(gross_returns))
    power: float = 1 / len(gross_returns)
    geometric_mean: float = product ** power
    return geometric_mean


def get_net_average(gross_average: float) -> float:
    """
    Convert gross average back to net average return.
    """
    net_average: float = gross_average - 1
    return net_average


def get_average_return(net_returns: Dict[str, float]) -> float:
    """
    Calculate average annual return from yearly net returns.
    """
    gross_returns: np.ndarray = get_gross_returns(net_returns)
    gross_average: float = get_geometric_mean(gross_returns)
    net_average: float = get_net_average(gross_average)
    return net_average


def demo_ibm_returns() -> None:
    ibm_yearly_returns: Dict[str, float] = {
        "2000": -0.2084,
        "2001": 0.4300,
        "2002": -0.3547,
    }

    average_return: float = get_average_return(ibm_yearly_returns)
    print(f"Average annual return: {average_return:.4f}")


if __name__ == "__main__":
    demo_ibm_returns()