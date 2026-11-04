#Two sets contain the names of students attending two different classes. Find students
#who are present in both classes, students present only in the first class, students
#present only in the second class, and students present in at least one class.
classA = {"Rahul", "Priya", "Amit", "Sneha", "Neha"}
classB = {"Priya", "Amit", "Kiran", "Neha", "Ravi"}

print("Class A :", classA)
print("Class B :", classB)

print("Students in both classes :", classA & classB)
print("Only in Class A :", classA - classB)
print("Only in Class B :", classB - classA)
print("Students in at least one class:")
print(classA | classB)