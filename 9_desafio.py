__autor__ = "Jivaldo Da Cruz"

lista = []

for x in range(3):
    lista.append(int(input(f"Informe {x + 1}º número: ")))

lista.sort()#onde vão organizar os números
print("A ordem dos números são: ",lista)
