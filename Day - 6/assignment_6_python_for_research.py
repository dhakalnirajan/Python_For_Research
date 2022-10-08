# -*- coding: utf-8 -*-
"""Assignment - 6 - Python For Research.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1av5qpU31g2lx84S8q-pH2EPhV0FFcbgd

# 1. Define a class Square which has 3 methods: 
First calculate_area() and <br>
Second  calculate_volume() <br>
Third display_area_and_vol()

Create an object of a class and display the area and volume of the object. Take object attribute values from the user.
"""

class Square:
    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height
    
    def calculate_area(self):
        return self.length * self.breadth
    
    def calculate_volume(self):
        return self.length * self.breadth * self.height
    
    def display_area_and_vol(self):
        print("Area of the square is: ", self.calculate_area())
        print("Volume of the square is: ", self.calculate_volume())   # Technically, any square that has volume is cube. But here, we consider square == cube.

length = int(input("Enter the length of the square: "))
breadth = int(input("Enter the breadth of the square: "))
height = int(input("Enter the height of the square: "))

square = Square(length, breadth, height)
square.display_area_and_vol()

"""# 2. Write a Python class named Student with two attributes student_id, and student_name.
Add a new attribute student_class. Create a function to display the entire attribute and its values in the Student class. 
"""

class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display(self):
        print("Student ID: ", self.student_id)
        print("Student Name: ", self.student_name)
        print("Student Class: ", self.student_class)

student = Student(1, "John", "10th")
student.display()

"""# 3. Write a Python class to get all possible unique subsets from a set of distinct integers. 
Input : [4, 5, 6] <br>
Output : [ [], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6] ]

Output might be in any order.
"""

class unique_subsets:
    def __init__(self, list_of_numbers):
        self.list_of_numbers = list_of_numbers

    def get_subsets(self):
        return self.subsets_recur([], sorted(self.list_of_numbers))

    def subsets_recur(self, current, list_of_numbers):
        if list_of_numbers:
            return self.subsets_recur(current, list_of_numbers[1:]) + self.subsets_recur(current + [list_of_numbers[0]], list_of_numbers[1:])
        return [current]

print(unique_subsets([4, 5, 6]).get_subsets())

"""# 4. Write a Python class to reverse a string word by word.
Input string : 'hello .py'   <br>
Expected Output: '.py hello'
"""

class ReverseString:
    def __init__(self, string):
        self.string = string

    def reverse_string(self):
        return ' '.join(reversed(self.string.split()))

if __name__ == '__main__':
    string = 'hello .py'
    reverse_string = ReverseString(string)
    print(reverse_string.reverse_string())