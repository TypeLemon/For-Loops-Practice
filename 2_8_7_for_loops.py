total = 0

for i in range(3):
  price = float(input("Please enter the price of the product: "))
  quantity = int(input("Please enter the quantity of product: "))
  total += price*quantity

with_tax = round(total * 1.13, 2)
print("Total cost: $", with_tax) 