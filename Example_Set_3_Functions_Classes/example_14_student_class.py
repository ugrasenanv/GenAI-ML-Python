"""Example 14: Object-Oriented Programming - Student Class Implementation

Class Implementation:
- Defines a Student class with attributes and methods
- Demonstrates object-oriented programming (OOP) principles
- Shows encapsulation of data (attributes) and behavior (methods)
- Implements constructor (__init__) and custom methods
- Creates and manipulates objects of the Student class

Object-Oriented Programming Concepts:
1. Class: Blueprint or template for creating objects
2. Object: Instance of a class with specific data
3. Attributes: Data/properties stored in the object
4. Methods: Functions that operate on the object's data
5. Encapsulation: Bundling data and methods together

Class Structure Components:
- __init__ method: Constructor that initializes object attributes
- self parameter: Reference to the current instance of the class
- Instance attributes: name and marks stored in each object
- Instance methods: Functions that can access and modify object data

Constructor Method (__init__):
- Special method called automatically when object is created
- Takes 'self' as first parameter (refers to the object being created)
- Initializes object attributes with provided values
- Sets up the initial state of the object

Method Definition and Usage:
- Methods are functions defined inside a class
- First parameter is always 'self' (refers to the calling object)
- Can access and modify object attributes using self.attribute_name
- Called using object_name.method_name() syntax

Object Creation and Manipulation:
- Objects created using class_name(parameters)
- Each object has its own set of attributes
- Methods called on specific objects operate on that object's data
- Multiple objects can be created from the same class

Real-world Applications:
- Student management systems
- Educational record keeping
- User account management
- Data modeling and organization
- Software design and architecture

Concepts Covered:
- Class definition and structure
- Constructor implementation
- Instance attributes and methods
- Object creation and instantiation
- Method calling and object manipulation
- Encapsulation and data organization
"""

# Define the Student class
class Student:
    """
    Student class to represent a student with name and marks.
    
    Attributes:
        name (str): Student's name
        marks (float): Student's marks/score
    
    Methods:
        display(): Display student information
        get_grade(): Calculate and return grade based on marks
        update_marks(new_marks): Update student's marks
    """
    
    def __init__(self, name, marks):
        """
        Constructor to initialize Student object.
        
        Parameters:
            name (str): Student's name
            marks (float): Student's marks (0-100)
        """
        self.name = name
        self.marks = marks
        print(f"Student object created for {name} with marks {marks}")
    
    def display(self):
        """
        Display complete student information with formatting.
        """
        print(f"\n{'='*30}")
        print(f"    STUDENT INFORMATION")
        print(f"{'='*30}")
        print(f"Name  : {self.name}")
        print(f"Marks : {self.marks}/100")
        print(f"Grade : {self.get_grade()}")
        print(f"Status: {self.get_status()}")
        print(f"{'='*30}")
    
    def get_grade(self):
        """
        Calculate and return grade based on marks.
        
        Returns:
            str: Grade (A+, A, B, C, D, or F)
        """
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"
    
    def get_status(self):
        """
        Determine pass/fail status based on marks.
        
        Returns:
            str: "Pass" or "Fail"
        """
        return "Pass" if self.marks >= 50 else "Fail"
    
    def update_marks(self, new_marks):
        """
        Update student's marks with validation.
        
        Parameters:
            new_marks (float): New marks value (0-100)
        """
        if 0 <= new_marks <= 100:
            old_marks = self.marks
            self.marks = new_marks
            print(f"Marks updated for {self.name}: {old_marks} -> {new_marks}")
        else:
            print("Invalid marks! Please enter marks between 0 and 100.")
    
    def __str__(self):
        """
        String representation of Student object.
        
        Returns:
            str: Formatted student information
        """
        return f"Student(name='{self.name}', marks={self.marks}, grade='{self.get_grade()}')"


# Demonstrate class usage with multiple objects
print("=== STUDENT CLASS DEMONSTRATION ===")

# Create student objects
print("\n1. Creating Student Objects:")
student1 = Student("Alice Johnson", 85)
student2 = Student("Bob Smith", 92)
student3 = Student("Carol Davis", 67)

# Display student information
print("\n2. Displaying Student Information:")
student1.display()
student2.display()
student3.display()

# Demonstrate method usage
print("\n3. Method Usage Examples:")
print(f"Student 1 Grade: {student1.get_grade()}")
print(f"Student 2 Status: {student2.get_status()}")
print(f"Student 3: {student3}")

# Demonstrate marks update
print("\n4. Updating Student Marks:")
student1.update_marks(95)
student1.display()

# Create interactive student
print("\n5. Interactive Student Creation:")
try:
    name = input("Enter student name: ")
    marks = float(input("Enter student marks (0-100): "))
    
    if 0 <= marks <= 100:
        interactive_student = Student(name, marks)
        interactive_student.display()
    else:
        print("Invalid marks entered!")
except ValueError:
    print("Invalid input! Please enter numeric marks.")

print("\n=== CLASS DEMONSTRATION COMPLETE ===")