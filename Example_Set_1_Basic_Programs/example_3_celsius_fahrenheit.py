"""Example 3: Temperature Conversion (Celsius to Fahrenheit)

Function Implementation:
- Takes temperature input in Celsius scale from user
- Applies the temperature conversion formula
- Converts Celsius to Fahrenheit using mathematical relationship
- Displays the converted temperature with proper formatting

Mathematical Formula: F = (C × 9/5) + 32
Where:
- F = Temperature in Fahrenheit
- C = Temperature in Celsius
- 9/5 = Conversion ratio between scales
- 32 = Offset for Fahrenheit scale starting point

Temperature Scale Relationship:
- Water freezes at 0°C = 32°F
- Water boils at 100°C = 212°F
- Formula converts between these two temperature scales

Concepts Covered:
- Mathematical formula implementation
- Float arithmetic and precision
- Temperature scale conversions
- Formatted output display
"""

# Get temperature input from user
celsius = float(input("Enter temperature in Celsius: "))

# Apply conversion formula
fahrenheit = (celsius * 9/5) + 32

# Display converted temperature
print(f"Temperature in Fahrenheit = {fahrenheit}°F")
print(f"{celsius}°C is equal to {fahrenheit}°F")