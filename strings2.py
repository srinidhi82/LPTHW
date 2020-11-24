formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("ball", "bats", "wicks", "pads"))
print(formatter.format(22, "You have it", "Best", 11))
print(formatter.format(True, False, False, True))
# Combine escape char along with formatter
print(formatter.format("\nJan", "\aBang", "Hi I'am \"super\" tall", "\tcat"))
