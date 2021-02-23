num_of_num = int(input("How many numbers do you want to add?: "))
sum = 0

for i in range(num_of_num):
  user_num = int(input("Enter number: "))
  sum = sum + user_num

print("Sum:", sum) 