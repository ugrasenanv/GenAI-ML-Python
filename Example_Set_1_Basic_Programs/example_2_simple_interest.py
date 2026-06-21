"""Example 2: Simple Interest Calculator

Function Implementation:
- Takes user input for principal amount, rate of interest, and time period
- Applies the simple interest formula to calculate interest earned
- Uses float data type to handle decimal values for precise calculations
- Displays the calculated simple interest amount

Mathematical Formula: SI = (Principal × Rate × Time) / 100
Where:
- Principal (P): The initial amount of money
- Rate (R): The annual interest rate (as a percentage)
- Time (T): The time period (in years)

Concepts Covered:
- Input/output operations with type conversion
- Mathematical formula implementation
- Float arithmetic operations
- Variable assignment and calculations
"""

# Get financial details from user
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))

# Calculate simple interest using the formula
simple_interest = (principal * rate * time) / 100

# Display the calculated result
print("Simple Interest =", simple_interest)
print(f"Total Amount = {principal + simple_interest}")