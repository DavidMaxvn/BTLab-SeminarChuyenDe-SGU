import numpy as np


def average_portfolio_return(net_returns):
    """Compute the geometric average return from a series of net returns."""
    if not isinstance(net_returns, (list, tuple, np.ndarray)):
        raise TypeError("net_returns must be list/tuple/ndarray")
    if len(net_returns) == 0:
        raise ValueError("net_returns must not be empty")

    gross_returns = []
    for r in net_returns:
        try:
            r = float(r)
        except (TypeError, ValueError):
            raise ValueError(f"Invalid return: {r}")
        gross = 1.0 + r
        if gross <= 0:
            raise ValueError(f"Gross return must be > 0, got {gross}")
        gross_returns.append(gross)

    geo_mean = np.prod(gross_returns) ** (1.0 / len(gross_returns))
    return geo_mean - 1.0


if __name__ == '__main__':
    data = [0.05, -0.02, 0.03, 0.08]
    print('Average portfolio return:', average_portfolio_return(data))
