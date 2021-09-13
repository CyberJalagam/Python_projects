salary = int(input("Employee salary: "))

hra = (salary * 10)/100
ta = (salary * 5)/100
ma = (salary * 15)/100

total_salary = hra + ta + ma + salary

print("HRA: ",hra)
print("TA: ",ta)
print("MA: ",ma)
print("Total salary: ",total_salary)
