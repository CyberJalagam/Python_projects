'''
write program to generate folloing series with its sum
x+x^2+X^3..........X^n
you have to accept x & n
'''

n = int(input("Enter n: "))
x = int(input("Enter x: "))

org_num = x
n = n + 1

for num in range(2,n):
    x = x + org_num ** num

print("sum: ",x)

