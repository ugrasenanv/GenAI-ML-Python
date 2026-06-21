"""Example 8: Sum of First 10 Natural Numbers

Implementation Details:
- Uses for loop to iterate through numbers 1 to 10
- Accumulates sum using compound assignment operator (+=)
- Demonstrates range function with start and stop parameters
- Shows loop-based accumulation pattern

Algorithm:
1. Initialize sum variable to 0
2. Use for loop with range(1, 11) for numbers 1 to 10
3. Add each number to running sum
4. Display final accumulated sum

Concepts: For loops, range function, accumulator pattern, compound operators
"""

# Initialize accumulator variable
sum = 0

# Loop through natural numbers 1 to 10
for i in range(1, 11):
    sum += i  # Add current number to sum

# Display the final result
print("Sum of first 10 natural numbers =", sum)