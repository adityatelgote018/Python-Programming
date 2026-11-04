#Problem Statement: Accept length and width and calculate area and perimeter.

length = float(input("Enter Length: "))
width = float(input("Enter Width: "))

area = length * width
perimeter = 2 * (length + width)

print("Area =", area)
print("Perimeter =", perimeter)