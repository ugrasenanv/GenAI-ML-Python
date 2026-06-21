"""Example 5: Calculate Square and Cube of a Number

Function Implementation:
- Takes a numerical input from the user
- Calculates the square using the exponentiation operator (**)
- Calculates the cube using the exponentiation operator (**)
- Displays both results with clear labels

Mathematical Concepts:
- Square: A number multiplied by itself (n² = n × n)
- Cube: A number multiplied by itself three times (n³ = n × n × n)
- Exponentiation: Raising a number to a specific power

Python Exponentiation Operator (**):
- ** is the power/exponentiation operator in Python
- num ** 2 calculates num to the power of 2 (square)
- num ** 3 calculates num to the power of 3 (cube)
- More efficient than repeated multiplication for powers

Geometric Interpretation:
- Square: Area of a square with side length 'num'
- Cube: Volume of a cube with side length 'num'

Concepts Covered:
- Exponentiation operations
- Mathematical power calculations
- Multiple calculations from single input
- Power operator usage (**)
- Geometric mathematical relationships
"""

# Get number input from user
number = float(input("Enter a number: "))

# Calculate square and cube using power operator
square = number ** 2
cube = number ** 3

# Display results with detailed formatting
print(f"\nCalculations for {number}:")
print(f"Square ({number}²) = {square}")
print(f"Cube ({number}³) = {cube}")
print(f"\nUsing multiplication:")
print(f"Square = {number} × {number} = {number * number}")
print(f"Cube = {number} × {number} × {number} = {number * number * number}")