"""
===============================================================================
PYTHON DATA STRUCTURES – LEARNING PROGRAM
===============================================================================

This file is designed to teach Python data structures in depth.

Covered Data Structures:
1. String
2. Array (from array module)
3. List
4. Tuple
5. Dictionary
6. Set

For EACH data structure, you will find:
- 1 Beginner example
- 2 Intermediate examples
- 1 Advanced example (mixing data types and/or structures)

You are encouraged to:
- Read comments carefully
- Modify values and re-run
- Print intermediate results
===============================================================================
"""

# =============================================================================
# SECTION 1: STRINGS
# =============================================================================

print("\n==================== STRINGS ====================\n")

# -------------------------------------------------------------------------
# Example 1 (Beginner): Basic String Creation and Access
# -------------------------------------------------------------------------

name = "Python"

print("The string is:", name)
print("First character:", name[0])
print("Last character:", name[-1])
print("Length of string:", len(name))

# Strings are IMMUTABLE
# name[0] = 'J'  # ❌ This would cause an error


# -------------------------------------------------------------------------
# Example 2 (Intermediate): String Methods and Formatting
# -------------------------------------------------------------------------

sentence = "python is amazing"

capitalized = sentence.capitalize()
upper_case = sentence.upper()
replaced = sentence.replace("amazing", "powerful")

print("\nOriginal:", sentence)
print("Capitalized:", capitalized)
print("Uppercase:", upper_case)
print("Replaced:", replaced)

language = "Python"
version = 3.12
formatted = f"{language} version {version} is widely used"

print("Formatted string:", formatted)


# -------------------------------------------------------------------------
# Example 3 (Intermediate): Splitting and Joining Strings
# -------------------------------------------------------------------------

data = "apple,banana,orange,grapes"

fruits_list = data.split(",")
print("\nSplit into list:", fruits_list)

joined_string = " | ".join(fruits_list)
print("Joined string:...", joined_string)


# -------------------------------------------------------------------------
# Example 4 (Advanced): String + List + Dictionary
# -------------------------------------------------------------------------

log_data = "ERROR:404:Page not found"

parts = log_data.split(":")
log_entry = {
    "level": parts[0],
    "code": int(parts[1]),
    "message": parts[2]
}

print("\nAdvanced String Example:...")
print(log_entry)
# =============================================================================
# SECTION 2: ARRAYS
# =============================================================================

print("\n==================== ARRAYS ====================\n")

from array import array

# -------------------------------------------------------------------------
# Example 1 (Beginner): Creating and Accessing an Array
# -------------------------------------------------------------------------

numbers = array('i', [1, 2, 3, 4])

print("Array contents:", numbers)
print("First element:", numbers[0])


# -------------------------------------------------------------------------
# Example 2 (Intermediate): Array Operations
# -------------------------------------------------------------------------

numbers.append(5)
numbers.remove(2)

print("\nAfter append and remove:", numbers)

for num in numbers:
    print("Number:", num)


# -------------------------------------------------------------------------
# Example 3 (Intermediate): Mathematical Processing
# -------------------------------------------------------------------------

squares = array('i', [])

for n in numbers:
    squares.append(n * n)

print("\nSquares array:", squares)


# -------------------------------------------------------------------------
# Example 4 (Advanced): Array + List + Dictionary
# -------------------------------------------------------------------------

sensor_readings = array('f', [23.5, 24.1, 22.8])

sensor_report = {
    "unit": "Celsius",
    "readings": list(sensor_readings),
    "average": sum(sensor_readings) / len(sensor_readings)
}

print("\nAdvanced Array Example:")
print(sensor_report)
print(log_entry)

# =============================================================================
# SECTION 3: LISTS
# =============================================================================

print("\n==================== LISTS ====================\n")

# -------------------------------------------------------------------------
# Example 1 (Beginner): Creating and Modifying a List
# -------------------------------------------------------------------------

animals = ["dog", "cat", "elephant"]

animals.append("tiger")
animals[1] = "lion"

print("Animals list:", animals)


# -------------------------------------------------------------------------
# Example 2 (Intermediate): List Slicing and Iteration
# -------------------------------------------------------------------------

numbers_list = [10, 20, 30, 40, 50]

print("\nFirst three:", numbers_list[:3])
print("Last two:", numbers_list[-2:])

total = 0
for n in numbers_list:
    total += n

print("Total sum:", total)


