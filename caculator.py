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
print("Available operations:                                     =")
print("===========================================================")
print("=   + (Add)                                               =")
print("=   - (Subtract)                                          =")
print("=   / (Divide)                                            =")
print("=   ** (Power - Second number)                            =")
print("===========================================================")

first = float(input("First number: "))
second = float(input("Second number: "))
add = first + second
sub = first - second
div = first / second
rem = first % second
power = first ** second
divr = first // second
operator = (input("Enter the operator: ")) 

if operator == "+":
    final = add
    key = "Addition: "

elif operator == "-":
    final = sub
    key = "Subtraction: "

elif operator == "/":
    final_quo = div
    final_rem = rem
    print("Quotient: " + str(final_quo))
    print("Remainder:" + str(final_rem))

elif operator == "**":
    final = power
    key = "Power: "

else:
    final = "Invalid operator"
    key = "Error: "

print(key + str(final))

print("<<<<< © RB INTERNATIONAL NETWORK™ >>>>>")
