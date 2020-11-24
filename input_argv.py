# this is combo of script and argv

from sys import argv
script, thingy = argv
prompt = '- '
print(f"Hi {thingy}, I'm the {script} script.")
print(f"Do you like me {thingy} ?")
live = input(prompt)
print(f"Where do you live {thingy}")
live = input(prompt)

print(f"Which computer you have ? ")
computer = input(prompt)

print(f""" \tSo you are {thingy} , you live in
      {live} and you own {computer}
      wow ,some update
      """)
