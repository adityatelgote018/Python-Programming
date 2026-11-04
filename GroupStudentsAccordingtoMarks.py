#Create a dictionary containing student names and marks. Divide the students into three
#categories using dictionaries or lists:
# Distinction: 75 and above
# First Class: 60–74
# Pass Class: 40–59
#Display the students in each category.
students = {
    "Rahul": 82,
    "Priya": 68,
    "Amit": 55,
    "Sneha": 91,
    "Neha": 73,
    "Kiran": 45
}
distinction = []
first_class = []
pass_class = []
print("Student Marks:")
for name in students:
    print(name, ":", students[name])
    if students[name] >= 75:
        distinction.append(name)
    elif students[name] >= 60:
        first_class.append(name)
    elif students[name] >= 40:
        pass_class.append(name)
print("Distinction:")
print(distinction)
print("First Class:")
print(first_class)
print("Pass Class:")
print(pass_class)