# Author: Zachary Klopp
# File Name: Module_2_Case_Study.py
# Description: Takes input of students last name and GPA and checks whether they made the Dean's list or Honor Role.

while True:
    student_last_name = input("Please input students last name or input ZZZ to stop: ")
    if student_last_name == "ZZZ":
        print("User inputted ZZZ so ending program.")
        break
    student_first_name = input("Please input the students first name: ")
    gpa = float(input("Please input the students GPA: "))
    if gpa >= 3.5:
        print(f"{student_first_name} {student_last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print (f"{student_first_name} {student_last_name} has made the Honor Roll.")
    else:
        print (f"{student_first_name} {student_last_name} has not made the Dean's List or Honor Roll.")