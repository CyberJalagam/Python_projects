print("===========================================================")
print("= Operators:                                              =")
print("===========================================================")
print("=  +        (Add)                                         =")
print("=  -        (Subtract),   (first - second)                =")
print("=  /        (Divide)                                      =")
print("=  **       (Power),      (first_number^second_number)    =")
print("=  *        (Multiply)                                    =")
print("=  %        (Modulus)                                     =")
print("===========================================================")

operator = (input("Enter the operator: "))

first = float(input("First number: "))
second = float(input("Second number: "))
add = first + second
sub = first - second
div = first / second
modulus = first % second
power = first ** second
divr = first // second
mul = first * second

if operator == "+":
    final = add
    key = "Addition: "
    
elif operator == "-":
    final = sub
    key = "Subtraction: "

elif operator == "/":
    final = div
    key = "Division: "

elif operator == "//":
    final = divr
    key = "Division: "

elif operator == "%":
    final = modulus
    key = "Modulus: "

elif operator == "**":
    final = power
    key = "Power: "

elif operator == "*":
    final = mul
    key = "Multiplication: "
    
else:
    final = "Invalid operator"
    key = "Error: "

print(f"{key} {final}")