__autor__ = "Jivaldo Da Cruz"

num_1 = float(input("Insira primeiro número: "))
num_2 = float(input("Insira segundo número: "))

total = (num_1 + num_2) / 2

if(total >= 9):
    print(f"{total} -> A")
elif(total >= 7.5):
    print(f"{total} -> B")
elif(total >= 6):
    print(f"{total} -> C")
elif(total >= 4):
    print(f"{total} -> D")
elif(total >= 0):
    print(f"{total} -> E")
    
