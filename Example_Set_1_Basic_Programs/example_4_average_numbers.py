"""Example 4: Calculate Average of Three Numbers

Function Implementation:
- Takes three numerical inputs from the user
- Adds all three numbers together to get the sum
- Divides the sum by 3 to calculate the arithmetic mean
- Displays the calculated average with appropriate precision

Mathematical Formula: Average = (Sum of all numbers) / (Count of numbers)
For three numbers: Average = (num1 + num2 + num3) / 3

Arithmetic Mean Concept:
- Average represents the central tendency of a dataset
- It's calculated by summing all values and dividing by count
- Useful for finding the typical value in a set of numbers
- Result may be a decimal even if all inputs are integers

Concepts Covered:
- Multiple input handling
- Addition and division operations
- Arithmetic mean calculation
- Float precision in results
- Sequential input processing
"""

# Get three numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Calculate sum and average
total_sum = num1 + num2 + num3
average = total_sum / 3

# Display results with detailed output
print(f"Numbers entered: {num1}, {num2}, {num3}")
print(f"Sum = {total_sum}")
print(f"Average = {average}")
print(f"Average (rounded to 2 decimals) = {average:.2f}")