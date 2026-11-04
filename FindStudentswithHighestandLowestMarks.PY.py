#Create a dictionary containing student names and their marks. Find and display the
#students having the highest and lowest marks.
students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78,
    "Sneha": 95,
    "Neha": 88
}
print("Student Marks:")
for name in students:
    print(name, ":", students[name])
highest = max(students.values())
lowest = min(students.values())
for name in students:
    if students[name] == highest:
        high_student = name
    if students[name] == lowest:
        low_student = name
print("Highest Marks :", highest)
print("Student :", high_student)
print("Lowest Marks :", lowest)
print("Student :", low_student)