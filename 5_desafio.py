__autor__ = "Jivaldo Da Cruz"

num_1 = float(input("Informe 1º nota: "))
num_2 = float(input("Informe 2º nota: "))

total = (num_1 + num_2) / 2

if(total < 10):
    print("Reprovado!")
elif(total > 10):
    print("Aprovado!")
else:
    print("Aprovado com Distinção!")
