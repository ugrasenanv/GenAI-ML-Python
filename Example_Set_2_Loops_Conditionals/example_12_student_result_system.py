"""Example 12: Complete Student Result Management System

Function Implementation:
- Collects comprehensive student information and academic data
- Processes marks for five subjects with validation
- Calculates total marks, percentage, and assigns grades
- Generates a detailed academic report with performance analysis
- Implements a complete grading system with multiple grade levels

Student Data Collection:
1. Personal Information: Name and Roll Number
2. Academic Performance: Marks in 5 subjects (out of 100 each)
3. Statistical Analysis: Total, percentage, average calculation
4. Grade Assignment: Based on percentage ranges

Grading System Implementation:
- A+ Grade: 90% and above (Excellent Performance)
- A Grade: 80-89% (Very Good Performance)
- B Grade: 70-79% (Good Performance)
- C Grade: 60-69% (Satisfactory Performance)
- D Grade: 50-59% (Pass but Needs Improvement)
- F Grade: Below 50% (Fail - Requires Re-examination)

Mathematical Calculations:
- Total Marks = Sum of all 5 subject marks
- Percentage = (Total Marks / Maximum Marks) × 100
- Maximum Marks = 5 subjects × 100 marks = 500 marks
- Average Marks = Total Marks / Number of Subjects

Conditional Logic Structure:
- Uses cascading if-elif-else statements
- Checks conditions from highest to lowest grade
- Ensures exclusive grade assignment
- Handles edge cases and boundary conditions

Real-world Applications:
- Academic management systems
- Educational record keeping
- Performance tracking and analysis
- Automated report card generation
- Student progress monitoring

Concepts Covered:
- Complex conditional statements
- Multi-level decision making
- Data collection and processing
- Mathematical calculations in programming
- Formatted output and report generation
- Real-world system simulation
"""

# Student Information Collection
print("=== STUDENT RESULT MANAGEMENT SYSTEM ===")
print("Please enter student details and marks:\n")

# Collect student identification
student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")

# Collect subject marks with validation
print("\nEnter marks for 5 subjects (out of 100 each):")
subjects = ["Mathematics", "Science", "English", "Social Studies", "Computer Science"]
marks = []

for i, subject in enumerate(subjects, 1):
    while True:
        try:
            mark = float(input(f"Enter marks in {subject}: "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Please enter marks between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

# Performance calculations
total_marks = sum(marks)
max_marks = len(marks) * 100
percentage = (total_marks / max_marks) * 100
average_marks = total_marks / len(marks)

# Grade determination using conditional logic
if percentage >= 90:
    grade = "A+"
    performance = "Excellent"
elif percentage >= 80:
    grade = "A"
    performance = "Very Good"
elif percentage >= 70:
    grade = "B"
    performance = "Good"
elif percentage >= 60:
    grade = "C"
    performance = "Satisfactory"
elif percentage >= 50:
    grade = "D"
    performance = "Pass (Needs Improvement)"
else:
    grade = "F"
    performance = "Fail (Re-examination Required)"

# Generate comprehensive report
print("\n" + "="*50)
print("           STUDENT ACADEMIC REPORT")
print("="*50)
print(f"Student Name    : {student_name}")
print(f"Roll Number     : {roll_number}")
print("-"*50)
print("SUBJECT-WISE PERFORMANCE:")
for i, (subject, mark) in enumerate(zip(subjects, marks), 1):
    print(f"{subject:<20}: {mark}/100")
print("-"*50)
print("ACADEMIC SUMMARY:")
print(f"Total Marks     : {total_marks}/{max_marks}")
print(f"Percentage      : {percentage:.2f}%")
print(f"Average Marks   : {average_marks:.2f}")
print(f"Grade Achieved  : {grade}")
print(f"Performance     : {performance}")
print("="*50)

# Additional analysis
if percentage >= 75:
    print("🎉 CONGRATULATIONS! Outstanding academic performance!")
elif percentage >= 60:
    print("👍 Good work! Keep up the consistent effort!")
elif percentage >= 50:
    print("📚 Focus on improvement. You can do better!")
else:
    print("⚠️  Need significant improvement. Consider additional study support.")

# Subject-wise analysis
print(f"\nSUBJECT ANALYSIS:")
highest_mark = max(marks)
lowest_mark = min(marks)
best_subject = subjects[marks.index(highest_mark)]
weak_subject = subjects[marks.index(lowest_mark)]

print(f"Strongest Subject: {best_subject} ({highest_mark}/100)")
print(f"Weakest Subject : {weak_subject} ({lowest_mark}/100)")
print(f"Performance Range: {lowest_mark} - {highest_mark} marks")
print("="*50)