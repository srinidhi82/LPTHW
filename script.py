"""
This code is basically to demonstarte the use of argv as n argument passed
while executing python script.py
"""
from sys import argv
script, first, second, third = argv
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
