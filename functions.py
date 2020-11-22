def func1(x):
    return 8 *x

op = func1(5)
print(op)


def func2(a, b):
    return a - b

subtract = func2(20, 8)
print(subtract)

def bmi_calc(name, wt_kg, ht_m):
    bmi = wt_kg / (ht_m **2)
    
    print("bmi is ")
    print(bmi)
    

    if bmi > 25:
       return name + " is overweight"
    else:
        return name + " is not overweight"


Person1 = bmi_calc("Sri", 71, 1.70)
P2 = bmi_calc("Sam", 60, 1.62)
print (Person1)
print(P2)