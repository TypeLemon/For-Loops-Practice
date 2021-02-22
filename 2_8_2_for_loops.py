number = int(input("Enter a number: "))
total = 0

#start at 1, end at number + 1, increase by 2
for i in range(1, number + 1, 2):
    total = total + i

print(total)
