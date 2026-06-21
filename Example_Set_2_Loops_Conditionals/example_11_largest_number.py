"""Example 11: Find the Largest Among Three Numbers

Function Implementation:
- Takes three numerical inputs from the user
- Uses conditional statements to compare the numbers
- Implements logical AND operations for comprehensive comparison
- Determines and displays the largest number among the three

Comparison Logic Algorithm:
1. Compare first number with both second and third numbers
2. If first is greater than or equal to both others, it's largest
3. Otherwise, compare second number with first and third
4. If second is greater than or equal to both others, it's largest
5. If neither first nor second is largest, third must be largest

Conditional Structure:
- if: Check if 'a' is largest (a >= b AND a >= c)
- elif: Check if 'b' is largest (b >= a AND b >= c)
- else: If neither above is true, 'c' must be largest

Logical Operators Used:
- >= (Greater than or equal to): Handles equal values correctly
- AND (and): Both conditions must be true
- Chained comparisons ensure comprehensive checking

Edge Cases Handled:
- All three numbers are equal
- Two numbers are equal and larger than third
- Negative numbers comparison
- Decimal numbers comparison

Alternative Approaches:
- Using max() built-in function: max(a, b, c)
- Using nested if statements
- Using list and sort operations
- Using ternary operators for concise code

Concepts Covered:
- Conditional statements (if-elif-else)
- Logical operators (and, >=)
- Comparison operations
- Decision-making algorithms
- Multiple condition evaluation
- Input validation and processing
"""

# Get three numbers from user
print("=== Find the Largest Number ===")
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
third_number = float(input("Enter third number: "))

# Display the input numbers
print(f"\nNumbers entered: {first_number}, {second_number}, {third_number}")

# Determine the largest number using conditional logic
if first_number >= second_number and first_number >= third_number:
    largest = first_number
    position = "first"
elif second_number >= first_number and second_number >= third_number:
    largest = second_number
    position = "second"
else:
    largest = third_number
    position = "third"

# Display results with detailed information
print(f"\nComparison Results:")
print(f"Largest number = {largest}")
print(f"The {position} number ({largest}) is the largest.")

# Show comparison details
print(f"\nComparison Details:")
print(f"{first_number} vs {second_number}: {'First' if first_number >= second_number else 'Second'} is larger")
print(f"{first_number} vs {third_number}: {'First' if first_number >= third_number else 'Third'} is larger")
print(f"{second_number} vs {third_number}: {'Second' if second_number >= third_number else 'Third'} is larger")

# Handle special cases
if first_number == second_number == third_number:
    print(f"\nSpecial case: All three numbers are equal!")
elif first_number == second_number or first_number == third_number or second_number == third_number:
    print(f"\nSpecial case: Two numbers are equal and they are the largest!")

# Demonstrate alternative method
print(f"\nUsing Python's max() function: {max(first_number, second_number, third_number)}")