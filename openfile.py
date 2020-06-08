from sys import argv
"""
script, filename = argv

txt = open(filename)
print(f"Here is your file {filename} ")
print(txt.read())
"""
filename = input(" Please tel em the name of the file ")
filename = open(filename)
print(filename.read())
filename.close()
