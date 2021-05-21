#!/usr/bin/env python
#
# Copyright (C) 2020-2021 RB INTERNATIONAL NETWORK
#
#            An Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

print("<<<<< © RB INTERNATIONAL NETWORK™ >>>>>")

print("===========================================================")
print("Operator numbers:                                         =")
print("===========================================================")
print("=  1.     + (Add)                                         =")
print("=  2.     - (Subtract)                                    =")
print("=  3.     / (Divide)                                      =")
print("=  4.     ** (Power), (first_number^second_number)        =")
print("===========================================================")

operator = (input("Enter the operator number: ")) 

first = float(input("First number: "))
second = float(input("Second number: "))
add = first + second
sub = first - second
div = first / second
rem = first % second
power = first ** second
divr = first // second

if operator == "1":
    final = add
    key = "Addition: "

elif operator == "2":
    final = sub
    key = "Subtraction: "

elif operator == "3":
    final_quo = div
    final_rem = rem
    print("Quotient: " + str(final_quo))
    print("Remainder:" + str(final_rem))
    print("<<<<< © RB INTERNATIONAL NETWORK™ >>>>>")
    quit()

elif operator == "4":
    final = power
    key = "Power: "

else:
    final = "Invalid operator"
    key = "Error: "

print(key + str(final))

print("<<<<< © RB INTERNATIONAL NETWORK™ >>>>>")
