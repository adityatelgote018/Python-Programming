#Create a tuple containing student records (roll_no, name, marks). Sort the records
#according to marks in descending order and display the result.
students = (
    (101, "Rahul", 85),
    (102, "Priya", 92),
    (103, "Amit", 78),
    (104, "Sneha", 95)
)
print("Original Records:")
for student in students:
    print(student)
sorted_students = sorted(students, key=lambda x: x[2], reverse=True)
print("Records Sorted by Marks:")
for student in sorted_students:
    print(student)