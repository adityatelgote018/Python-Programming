#Create a list of student records where each record contains (roll_no, name, marks).
#Convert the student names into a set to find unique students. Create a dictionary
#mapping student names to marks. Finally, display the highest scorer, average marks,
#unique student names, and students who scored above the average.
students = [
    (101, "Rahul", 85),
    (102, "Priya", 92),
    (103, "Amit", 78),
    (104, "Sneha", 95),
    (105, "Neha", 80)
]
print("Student Records:")
print(students)
names = set()
marks = {}
for student in students:
    names.add(student[1])
    marks[student[1]] = student[2]
print("Unique Student Names:")
print(names)
print("Student Marks Dictionary:")
print(marks)
highest = max(marks.values())
for name in marks:
    if marks[name] == highest:
        highest_student = name
total = 0
for mark in marks.values():
    total = total + mark
average = total / len(marks)
print("Highest Scorer :", highest_student)
print("Highest Marks :", highest)
print("Average Marks :", average)
above_average = []
for name in marks:
    if marks[name] > average:
        above_average.append(name)
print("Students scoring above average:")
print(above_average)