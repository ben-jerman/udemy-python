# exercise-2.py
# Python Lists and Dicctionaries
#
# Author: Benjamin Jerman
# Date: 2021-10-14

# Lists:

student_grades = [9.1, 8.8, 5.4, 6.6, 7.2]


grade_sum = sum(student_grades)
student_num = len(student_grades)
average_grade = grade_sum / student_num

print(average_grade)

# Getting a first index of a first occurence of a value
# from a list:
print(student_grades.index(8.8))

# Get an element from a list:
print(student_grades[0])

# Get multiple items from a list:
# Remember - upper bound not included in python!
print(student_grades[3:5])

print(student_grades[:3])
print(student_grades[3:])

# Negative Index returns last item:
print(student_grades[-1])
print(student_grades[-2])

# Also works on strings:
my_string = "hello"
print(my_string)
print(my_string[:3])