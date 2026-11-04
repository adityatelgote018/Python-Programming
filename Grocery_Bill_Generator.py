#Problem Statement: Generate grocery bill using f-strings.

item1 = "Rice"
quantity1 = 2
price1 = 60

item2 = "Sugar"
quantity2 = 1
price2 = 45

item3 = "Milk"
quantity3 = 3
price3 = 30

total1 = quantity1 * price1
total2 = quantity2 * price2
total3 = quantity3 * price3

grand_total = total1 + total2 + total3

print("---------- GROCERY BILL ----------")
print(f"Item       Quantity   Price   Total")
print(f"{item1:<10} {quantity1:<10} ₹{price1:<6} ₹{total1}")
print(f"{item2:<10} {quantity2:<10} ₹{price2:<6} ₹{total2}")
print(f"{item3:<10} {quantity3:<10} ₹{price3:<6} ₹{total3}")
print("----------------------------------")
print(f"Grand Total: ₹{grand_total}")