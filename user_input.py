# Not good way of writing code for input() function
"""
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} years old , {height} tall and {weight} heavy")
"""
#re-writing the above using input function with arguments asking users the question
"""
name = input("What is your name ? ")
age = input("How old are you ? ")
weight = input("What is your weight ? ")
height = input("How tall are you ? ")

print(f"Hi {name}, So you're {age} years old , {height} cms tall and {weight} kilos")
"""
#Lets ask avengers question to Dhruva
# IMPORTANT, more string formatting

name = input("What is your name ? ")
fav_avenger = input("who is your favorite avenger ? ")
iron_man = input("What happens to iron man in end game ? ")
cap_america = input("Is Captain AMerica still young ? ")
ant_man = input("Is ant man an avnger super hero ? ")
thor = input("Which Thor movie you like ? ")

print(f"Hi {name}, {fav_avenger} is your favorite , {iron_man}, \
{cap_america} is old \"wow\", {ant_man} is an avnger ? and {thor} is your fav movie!")