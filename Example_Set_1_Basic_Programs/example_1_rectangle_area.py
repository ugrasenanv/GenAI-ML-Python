"""Example 1: Rectangle Area Calculator

Implementation Details:
- Takes user input for rectangle dimensions (length and breadth)
- Applies basic multiplication formula for area calculation
- Uses float data type for decimal precision
- Displays the calculated area with formatted output

Mathematical Formula: Area = length × breadth
Concepts: Basic I/O operations, arithmetic operations, variable assignment
"""

# Get rectangle dimensions from user
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

# Calculate area using multiplication
area = length * breadth

# Display the result
print("Area of rectangle =", area)