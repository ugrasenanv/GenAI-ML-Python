"""Example 10: Fibonacci Series Generation

Function Implementation:
- Takes the number of terms to generate from user
- Uses two variables to track the previous two numbers
- Generates sequence where each number is sum of previous two
- Displays the complete Fibonacci series up to n terms

Fibonacci Sequence Definition:
- Starts with 0 and 1
- Each subsequent number = sum of the two preceding numbers
- Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
- Mathematical notation: F(n) = F(n-1) + F(n-2)

Algorithm Implementation:
1. Initialize first two numbers: a = 0, b = 1
2. For each term in the sequence:
   - Print current number (a)
   - Calculate next number: c = a + b
   - Update variables: a = b, b = c
3. Repeat for n iterations

Variable Update Mechanism:
- Current state: a = F(n), b = F(n+1)
- Next calculation: c = F(n) + F(n+1) = F(n+2)
- State update: a = F(n+1), b = F(n+2)
- This shifts the "window" forward in the sequence

Mathematical Properties:
- Golden ratio relationship: F(n+1)/F(n) approaches φ (phi) = 1.618...
- Appears frequently in nature (flower petals, spiral shells)
- Used in algorithms, art, and architecture

Applications:
- Algorithm design and analysis
- Natural pattern modeling
- Mathematical sequence studies
- Computer science recursion examples

Concepts Covered:
- Sequence generation using loops
- Variable swapping and state management
- Mathematical series implementation
- Pattern recognition in programming
- Iterative approach to recursive problems
"""

# Get number of terms from user
n = int(input("Enter number of Fibonacci terms to generate: "))

# Input validation
if n <= 0:
    print("Please enter a positive number.")
elif n == 1:
    print("Fibonacci Series: 0")
else:
    # Initialize the first two Fibonacci numbers
    first = 0
    second = 1
    
    print(f"\nFirst {n} terms of Fibonacci Series:")
    
    # Handle the sequence generation
    for i in range(n):
        if i == 0:
            print(first, end=" ")
            current = first
        elif i == 1:
            print(second, end=" ")
            current = second
        else:
            # Calculate next Fibonacci number
            current = first + second
            print(current, end=" ")
            
            # Update for next iteration
            first = second
            second = current
    
    print()  # New line after series
    
    # Show the pattern for educational purposes
    if n >= 3:
        print(f"\nPattern: Each number = sum of previous two numbers")
        print(f"Example: {second} = {first} + {second - first}")
        
    # Display mathematical properties for larger sequences
    if n >= 5:
        ratio = second / first if first != 0 else 0
        print(f"\nGolden Ratio approximation: {second}/{first} = {ratio:.6f}")
        print(f"Golden Ratio (φ): 1.618034...")