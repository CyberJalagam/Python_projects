mark_1 = float(input("Enter mark 1: "))
mark_2 = float(input("Enter mark 2: "))
mark_3 = float(input("Enter mark 3: "))

total = mark_1 + mark_2 + mark_3
average = total / 3

if total >= 70:
    grade = "A"
elif total >= 50:
    grade = "B"
elif total >= 33:
    grade = "C"
else:
    grade = "Failed"

print(f"Total marks : {total}")
print(f"Average : {average}")
print(f"Grade : {grade}")
