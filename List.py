Doctors=["Sharvari","Aditya","Lekha","Prajwal","Jaee","Anshul","Anandi","Dhruv"]
#Access Element.
print("Doctors :",Doctors)
print("First Doctor :",Doctors[0])
print("Last Doctor :",Doctors[-1])
print("Doctor from index 2 to 5 :",Doctors[2:6])
print("Reversed Order of Doctors :",Doctors[::-1])

#Modify Element.
Doctors[2]="Rahul"
Doctors[-1]="Priya"
print("Modified Doctors List :",Doctors)

#Adding Element.
Doctors.append("Amit")
print("After Append :",Doctors)
Doctors.insert(2,"Sneha")
print("After Insert :",Doctors)
Doctors.extend(["Kiran","Neha"])
print("After Extend :",Doctors)
new_Doctors=Doctors + ["Kiran","Neha"]
print("After Concatenate :",new_Doctors)

#Removing Element.
if "Rahul" in Doctors:
    Doctors.remove("Rahul")
print("After Removing Rahul :",Doctors)
Doctors.pop(4)
print("After the removing 4th Index :  ",Doctors)
Doctors.pop()
print("After Removing Last Index :  ",Doctors)
del Doctors[2:5]
print("After Deleting Index 2 to 4 :",Doctors)

#Searching And Counting.
if "Amit" in Doctors:
    print("Index of Amit:", Doctors.index("Amit"))
else:
    print("Amit is not in List.")
print("Numbers of time Priya Appears :",Doctors.count("Priya"))

#Sorting and Reversing.
Doctors.sort()
print("Ascending Order :",Doctors.sort())
Doctors.sort(  reverse = True )
print("Descending order :",Doctors)
Doctors.reverse()
print("After Reversed :",Doctors)
Doctors.clear()
print("After Clearing :",Doctors)






