# Problem 1: Student Grades Tracker
import numpy as np
students = [
    ("Alice", [85, 90, 78, 92]),
    ("Bob", [60, 65, 70, 75]),
    ("Charlie", [40, 45, 50, 55]),
    ("David", [95, 100, 98, 92])
]

students_dict = dict(students) 
avg = []  
for name, marks in students_dict.items():
    each_student_marks = np.sum(marks)  
    avg_marks = each_student_marks/len(marks)
    avg.append(avg_marks)  
    print(f"The average of {name} is {avg_marks}")
print()

max = avg[0]
for ele in avg:
    if ele > max:
        max = ele
        top_student = name
print("The highest grade is",max,"achieved by",name)

c = 0
names = students_dict.keys()
names = list(names)
di = dict(zip(names,avg))
passed_students = []
for name,value in di.items():
    if value > 50:
        c += 1
        passed_students.append(name)
print("The number of students passed are",c,"they are",passed_students)

