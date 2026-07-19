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