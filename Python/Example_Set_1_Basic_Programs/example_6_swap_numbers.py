"""Example 6: Swap Two Numbers Without Using a Temporary Variable

Function Implementation:
- Takes two integer inputs from the user
- Performs swapping using arithmetic operations only
- No additional temporary variable needed for the swap
- Displays the values before and after swapping

Swapping Algorithm (Arithmetic Method):
1. Store sum of both numbers in first variable: a = a + b
2. Subtract new 'a' from original sum to get original 'a': b = a - b
3. Subtract new 'b' from sum to get original 'b': a = a - b

Step-by-Step Process:
- Original: a = x, b = y
- Step 1: a = x + y, b = y
- Step 2: a = x + y, b = (x + y) - y = x
- Step 3: a = (x + y) - x = y, b = x
- Result: a = y, b = x (swapped!)

Alternative Methods:
- Using temporary variable (traditional)
- Using XOR bitwise operations
- Using tuple unpacking (Python-specific): a, b = b, a

Concepts Covered:
- Variable manipulation without extra storage
- Arithmetic operations for logical operations
- Memory-efficient programming techniques
- Mathematical approach to swapping
- Understanding variable assignment sequence
"""

# Get two numbers from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Display original values
print(f"\nBefore swapping:")
print(f"a = {a}")
print(f"b = {b}")

# Perform swapping without temporary variable
print(f"\nSwapping process:")
print(f"Step 1: a = a + b = {a} + {b} = {a + b}")
a = a + b
print(f"Step 2: b = a - b = {a} - {b} = {a - b}")
b = a - b
print(f"Step 3: a = a - b = {a} - {b} = {a - b}")
a = a - b

# Display swapped values
print(f"\nAfter swapping:")
print(f"a = {a}")
print(f"b = {b}")

# Demonstrate Python's elegant method
print(f"\nPython's elegant method: a, b = b, a")