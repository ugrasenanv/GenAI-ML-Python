"""Example 9: Factorial Calculation Using Loops

Function Implementation:
- Takes a positive integer input from the user
- Uses a for loop to multiply numbers from 1 to n
- Accumulates the product in a factorial variable
- Displays the calculated factorial result

Mathematical Definition:
- Factorial of n (n!) = 1 × 2 × 3 × ... × n
- Special cases: 0! = 1, 1! = 1
- Only defined for non-negative integers
- Grows very rapidly (4! = 24, 5! = 120, 10! = 3,628,800)

Algorithm Steps:
1. Initialize factorial variable to 1
2. Use for loop from 1 to n (inclusive)
3. Multiply factorial by each number in the sequence
4. Continue until all numbers are processed
5. Display the final accumulated result

Loop Mechanics:
- range(1, num + 1) generates numbers from 1 to num
- Compound assignment operator (*=) multiplies and assigns
- Each iteration: fact = fact * i
- Accumulator pattern: building result through iterations

Applications:
- Combinatorics and permutation calculations
- Mathematical series and sequences
- Probability theory computations
- Algorithm complexity analysis

Concepts Covered:
- For loops with range function
- Accumulator pattern implementation
- Compound assignment operators (*=)
- Mathematical sequence processing
- Iterative multiplication technique
"""

# Get positive integer from user
number = int(input("Enter a positive integer: "))

# Input validation
if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0 or number == 1:
    print(f"Factorial of {number} = 1")
else:
    # Initialize factorial accumulator
    factorial = 1
    
    # Show the calculation process
    calculation_steps = []
    
    # Calculate factorial using for loop
    for i in range(1, number + 1):
        factorial *= i
        calculation_steps.append(str(i))
    
    # Display results with detailed information
    print(f"\nCalculating {number}! (factorial of {number}):")
    print(f"Formula: {number}! = {' × '.join(calculation_steps)}")
    print(f"Result: {number}! = {factorial}")
    
    # Show step-by-step calculation for small numbers
    if number <= 5:
        print(f"\nStep-by-step calculation:")
        temp_fact = 1
        for i in range(1, number + 1):
            temp_fact *= i
            print(f"Step {i}: {i}! = {temp_fact}")