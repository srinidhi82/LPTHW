"""
This code is basically to demonstarte the use of argv as an argument passed
while executing python script.py
python script.py one two three (4 argments passed as argv is assigned to 4 variables)
"""
from sys import argv
script, first, second, third = argv
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
