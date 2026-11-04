#Accept marks of a student and display the grade according to the following criteria:90–100 → A+ ; 75–89 → A ;60–74 → B ;50–59 → C ;40–49 → D ;Below 40 → Fail
marks=int(input("Enter the Marks:"))

if marks>=90 and marks<=100:
    print("Grade : A+")
elif marks>=75:
    print("Grade : A")
elif marks>=60:
    print("Grade : B")
elif marks>=50:
    print("Grade : C")
elif marks>=40:
    print("Grade : D")
else:
    print("Grade : Fail")