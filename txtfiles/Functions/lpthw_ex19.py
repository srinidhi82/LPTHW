def cheese_and_crisp(cheese_amount, crisp_packets):
    print(f"You have {cheese_amount} and {crisp_packets}")


def cheese_brand_and_crisp_name("cheese_brand", "crisp_name"):
    print(f"You have {cheese_brand} and {crisp_name}")


print("Pass any 2 arguments")
cheese_and_crisp(20, 50)
cheese_brand_and_crisp_name("Cottage cheese", "Tayto chips")

print("Use variables and its value as input to function")
cheese = 20
crisps = 60

cheese_and_crisp(cheese, crisps)

print("Can also pass math as arguments to function")
cheese_and_crisp(25 + 46, 40 - 10)

print("Combine both")
cheese_and_crisp(cheese + 20, crisps - 20)
