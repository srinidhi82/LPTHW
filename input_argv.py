#this is combo of script and argv

from sys import argv
script, user_name = argv
prompt = '-- '
print(f"Hi {user_name}, I'm the {script} script.")
print(f"Do you like me {user_name} ?")
likes = input(prompt)
print(f"Where do you live {user_name}")
lives = input(prompt)

print(f"Which computer you have ? ")
computer = input(prompt)

print(f""" \tSo you are {user_name} , you live in
      {lives} and you own {computer}
      wow ,some update
      """)
      