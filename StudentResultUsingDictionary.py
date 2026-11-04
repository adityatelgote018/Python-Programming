 #Create a nested dictionary containing student names and marks in three subjects.
#Calculate total marks, percentage, and result for every student. A student passes only if
#marks in all subjects are at least 40.
students = {
    "Rahul": {"Python": 80, "DBMS": 75, "Maths": 65},
    "Priya": {"Python": 90, "DBMS": 85, "Maths": 95},
    "Amit": {"Python": 35, "DBMS": 60, "Maths": 70}
}
print("Student Records:")
for name in students:
    print(name, ":", students[name])
print("Results:")
for name in students:
    marks = students[name]
    total = marks["Python"] + marks["DBMS"] + marks["Maths"]
    percentage = total / 3
    if marks["Python"] >= 40 and marks["DBMS"] >= 40 and marks["Maths"] >= 40:
        result = "Pass"
    else:
        result = "Fail"
    print(name)
    print("Total :", total)
    print("Percentage :", round(percentage, 2))
    print("Result :", result)