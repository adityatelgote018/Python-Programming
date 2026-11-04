Doctors=("Sharvari","Aditya","Lekha","Prajwal","Jaee","Anshul","Anandi","Dhruv")
print("Doctors :",Doctors)
print("Frist Doctor :",Doctors[0])
print("Last Doctor :",Doctors[-1])
print("Display the doctors From Index 2 to 5 :",Doctors[2:6])
print("Reversed Order of the Tuple :",Doctors[::-1])

#Check Immutability
#Doctors[2]="Amit"
#print(Doctors)

# Concatenation & Repetition
tuple1=["Sharvari","Aditya"]
tuple2=["Lekha","Prajwal"]

#Concatenation
combine=tuple1+tuple2
print("Concatenate Tuple :",combine)

#Repetition
repeated=tuple1 * 3
print("Repeated Tuple :",repeated)

#Tuple Unpacking
doctor_details=("Sharvari",25,"Cardiologist")
name,age,specialization=doctor_details
print("\nDoctor Details :")
print("Name :",name)
print("Age :",age)
print("specialization :",specialization)

#Using * to unpack multiple remaining values
doctor_info=("Aditya",30,"Surgeon","Cardiology","10 years Experience")
name,age,*details=doctor_info
print("\nUsing * for Tuple Unpacking:")
print("Name :",name)
print("Age :",age)
print("Remaining Details :",details)

#Membership Testing
print("\nMembership Testing:")
print("Is Amit in the tuple?" , "Amit" in Doctors)
print("Is Rakhi not in the tuple?" , "Rakhi" not in Doctors)

#Tuple Functions
patients_ages=(25,30,21,45,34,43,65,56)
print("\nPatients Age :",patients_ages)
print("Count of Age 30 :",patients_ages.count(30))
print("Index of first occurrence of 30:", patients_ages.index(30))
print("Maximum Age :",max(patients_ages))
print("Minimum Age :",min(patients_ages))
print("Sum of all Ages :",sum(patients_ages))
