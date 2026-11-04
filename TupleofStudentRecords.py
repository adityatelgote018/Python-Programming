#Create a tuple containing student records in the form (roll_no, name, marks). Display
#the student who has obtained the highest marks.
students = (
    (101, "Rahul", 85),
    (102, "Priya", 92),
    (103, "Amit", 78),
    (104, "Sneha", 95),
    (105, "Neha", 88)
)
print("Student Records:")
for student in students:
    print(student)
highest = students[0]
for student in students:
    if student[2] > highest[2]:
        highest = student
print("Student with highest marks:")
print("Roll No :", highest[0])
print("Name :", highest[1])
print("Marks :", highest[2])