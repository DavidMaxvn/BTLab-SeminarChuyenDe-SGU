def get_geometric_mean(*nums: float) -> float:
    """Return the geometric mean of a list of positive floating-point numbers."""
    if not nums:
        raise ValueError("At least one number must be provided.")
    for num in nums:
        if num <= 0:
            raise ValueError("All numbers must be positive.")
    product = 1.0
    for num in nums:
        product *= num
    return product ** (1 / len(nums))

# Example usage:
numbers = [2.0, 8.0, 4.0]
result = get_geometric_mean(*numbers)
print(f"Geometric mean of {numbers} is {result}")