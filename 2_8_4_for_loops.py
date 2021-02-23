start = int(input("Enter start: "))
end = int(input("Enter end: "))

if start < end:
  for i in range(start, end + 1):
    print(i)

if start >= end:
  for i in range(start, end - 1, -1):
    print(i)