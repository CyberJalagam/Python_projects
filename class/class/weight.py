
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

weight = float(input("Weight: "))
korl = input("(K)g or (L)bs: ")

if korl == "l":
    final = weight * 0.45
    key = "Your weight in lbs is: "
elif korl == "L":
    final = weight * 0.45
    key = "Your weight in Lbs is:  "
elif korl == "k":
    final = weight / 0.45
    key = "Your weight in Kg is:  "
elif korl == "K":
    final = weight / 0.45
    key = "Your weight in kg is:  "
else:
    final = "Input not recogonized, please enter a valid input"
    key = "Error: "

print(key + str(final))    

print("<<<<< © RB INTERNATIONAL NETWORK™ >>>>>")




    
