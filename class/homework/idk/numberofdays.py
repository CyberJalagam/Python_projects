x = int(input('Days worked by A: '))
y = int(input('Days worked by B: '))
z = int(input('Days worked by C: '))

days = (x * y * z) / (x * y + y * z + x * z)

print(f"Total days if all worked together: {days}")
