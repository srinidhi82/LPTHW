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

namea = "Sri"
wt_kga = 72
ht_ma = 1.70


Person1 = bmi_calc(namea, wt_kga, ht_ma)
print (Person1)