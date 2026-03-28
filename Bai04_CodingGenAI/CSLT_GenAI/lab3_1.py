# Part 1: Open the chat window and ask to explain the geometric mean.


# Part 2: Implement the geometric mean function for two floating-point numbers.
import math


def geometric_mean(a: float, b: float) -> float:
	"""Return the geometric mean of two positive floating-point numbers."""
	if a <= 0 or b <= 0:
		raise ValueError("Both numbers must be positive.")
	return math.sqrt(a * b)


# Part 3: Call
num1 = 2.0
num2 = 8.0
result = geometric_mean(num1, num2)

print(f"Geometric mean of {num1} and {num2} is {result}")

