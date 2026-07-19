print("hello to python3 and vscode")
import math

def calculate_factorial(number):
    """Calculates the factorial of a non-negative integer.

    Args:
        number (int): The number to calculate the factorial of.

    Returns:
        int or str: The factorial of the number, or an error message if the number is negative.
    """
    if number < 0:
        return "Factorial is not defined for negative numbers....."
    else:
        return math.factorial(number)

# Example usage:
num = 5
print(f"The factorial of {num} is {calculate_factorial(num)}")
# Output: The factorial of 5 is 120

def fibonacci(n: int) -> int:
  """Calculates the nth Fibonacci number.

  Args:
      n (int): The position of the Fibonacci number to calculate.
               Must be a non-negative integer.

  Returns:
      int: The nth Fibonacci number.
  """
  if n < 0:
    raise ValueError("Input must be a non-negative integer.")
  elif n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    a, b = 0, 1
    for _ in range(2, n + 1):
      a, b = b, a + b
    return b

# Example usage:
# print(fibonacci(0))  # Output: 0
# print(fibonacci(1))  # Output: 1
# print(fibonacci(2))  # Output: 1
# print(fibonacci(3))  # Output: 2
# print(fibonacci(10)) # Output: 55

