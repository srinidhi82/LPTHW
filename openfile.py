from sys import argv
script, filename = argv
txt = open(filename)
print(txt.read())

print("Read ur file again")
#file_location = Path('txtfiles/sample2.txt').exists()
#print(file_location)

file_again = input(" File location? ")
txt_again = open(file_again)
print(txt_again.read())

