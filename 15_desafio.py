__autor__ = "Jivaldo Da Cruz"

import math

def equacao():
    a = float(input("Informe o número que coresponde o A: "))
    if(a == 0):
        return False
    b = float(input("Informe o número que coresponde o B: "))
    c = float(input("Informe o número que coresponde o C: "))

    delta = (b**2) - 4 * a * c
    print(delta)
    if(delta < 0):
        print("Não possui raízes por delta ser negativo!")
        return False
    else:
        calc_1 = (-b + math.sqrt(delta)) / (2 * a)
        calc_2 = (-b - math.sqrt(delta)) / (2 * a)
        print("A equação possui duas raizes real")
        print(f"x1: {calc_1:.3}, x2: {calc_2:.3}")

equacao()
