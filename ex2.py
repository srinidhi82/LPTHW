#Variables and Names
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
ave_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available")
print("there will be", cars_not_driven, "empty cars today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", ave_passengers_per_car, "in each car.")