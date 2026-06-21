"""Example 7: Student Report Card Generator

Function Implementation:
- Collects student personal details (name and roll number)
- Takes marks input for three subjects
- Calculates total marks by summing all subject marks
- Calculates percentage based on total marks
- Generates a formatted report card display

Data Collection Process:
1. Student identification (name and roll number)
2. Academic performance (marks in three subjects)
3. Statistical calculations (total and percentage)
4. Formatted output generation

Calculation Methods:
- Total Marks: Sum of all subject marks
- Percentage: (Total Marks / Maximum Possible Marks) × 100
- Average Marks: Total Marks / Number of Subjects

Report Card Components:
- Student identification information
- Individual subject performance
- Overall academic statistics
- Professional formatting for readability

Real-world Applications:
- Academic record management
- Performance tracking systems
- Educational data processing
- Student information systems

Concepts Covered:
- String input handling and storage
- Multiple numerical inputs
- Mathematical calculations (sum, percentage)
- Formatted output with proper alignment
- Data organization and presentation
- Real-world data processing simulation
"""

# Collect student identification details
print("=== Student Report Card Generator ===")
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

# Collect academic performance data
print("\nEnter marks for three subjects (out of 100 each):")
subject1_marks = float(input("Enter marks in Subject 1: "))
subject2_marks = float(input("Enter marks in Subject 2: "))
subject3_marks = float(input("Enter marks in Subject 3: "))

# Perform academic calculations
total_marks = subject1_marks + subject2_marks + subject3_marks
max_marks = 300  # 3 subjects × 100 marks each
percentage = (total_marks / max_marks) * 100
average_marks = total_marks / 3

# Generate formatted report card
print("\n" + "="*40)
print("           STUDENT REPORT CARD")
print("="*40)
print(f"Student Name    : {student_name}")
print(f"Roll Number     : {roll_number}")
print("-"*40)
print("SUBJECT WISE MARKS:")
print(f"Subject 1       : {subject1_marks}/100")
print(f"Subject 2       : {subject2_marks}/100")
print(f"Subject 3       : {subject3_marks}/100")
print("-"*40)
print("ACADEMIC SUMMARY:")
print(f"Total Marks     : {total_marks}/{max_marks}")
print(f"Percentage      : {percentage:.2f}%")
print(f"Average Marks   : {average_marks:.2f}")
print("="*40)

# Add grade classification
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "F"
    
print(f"Grade Achieved  : {grade}")
print("="*40)