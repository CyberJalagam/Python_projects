first_no = int(input("Enter the first no: "))
second_no = int(input("Enter the second no: "))

if first_no > second_no:
    final = first_no - second_no
else:
    final = second_no - first_no

print(f"Difference: {final} ")