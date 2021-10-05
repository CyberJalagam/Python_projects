starting = int(input("Enter the starting number: "))
ending = int(input("Enter the ending number: "))
step = int(input("Enter the step value: "))

sum = 0
ending = ending + 1
for x in range(starting,ending,step):
    sum = x + sum
    print(x)
print(f"Sum: {sum}")