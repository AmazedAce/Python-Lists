# # -*- coding: utf-8 -*-
# """
# Created on Wed May 22 17:29:21 2024

# @author: Loren
# """


# 1. Python List Transformation


# grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
# grades.sort(reverse=True)
# print("Sorted grades in descending order:", grades)

# print("-----------------------")

# average_grade = sum(grades) / len(grades)
# print("Average grade:", average_grade)

# print("-----------------------")

# grades_with_failures = ["Failed" if grade < 80 else grade for grade in grades]
# print("Grades with 'Failed' for grades below 80:", grades_with_failures)




# 2. Advanced List Methods and Identity Operators 



# submitted = ["Alice", "Bob", "Charlie", "David"]
# attended = ["Charlie", "Eve", "Alice", "Frank"]

# both_submitted_and_attended = list(set(submitted) & set(attended))
# print("Students who both submitted their assignments and attended the class:", both_submitted_and_attended)

# print("-----------------------")

# are_identical = set(submitted) == set(attended)
# print("Are the two lists identical regardless of order?", are_identical)

# print("-----------------------")

# attended = [student for student in attended if student in submitted]
# print("Attended list after removing those who did not submit their assignment:", attended)



# 3. Advance Slicing Techniques

# temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# second_week_temperatures = temperatures[7:14]
# print("Temperatures for the second week:", second_week_temperatures)

# print("-----------------------")

# temperatures_above_100 = [temp for temp in temperatures if temp > 100]
# print("Temperatures above 100:", temperatures_above_100)

# print("-----------------------")

# reversed_temperatures = temperatures[::-1]
# fifth_to_tenth_reversed = reversed_temperatures[4:10]
# print("Temperatures from the 5th to the 10th day of the reversed list:", fifth_to_tenth_reversed)




# 4. Deep Dive into Python Lists

# print("-----------------------")

# students = ["John", "Doe", "Jane", "Smith"]
# grades = [85, 90, 78, 88]
# activities = ["Football", "Music", "Art", "Dance"]


# # Task 1
# for student, grade, activity in zip(students, grades, activities):
#     if grade < 80:
#         print(f'{student}, {grade}, {activity}')

# print("-----------------------")

# # Task 2
# students_approved = [student for student, grade in zip(students, grades) if grade >= 80]


# print("-----------------------")

# # Task 3
# print("Students approved:", students_approved)

