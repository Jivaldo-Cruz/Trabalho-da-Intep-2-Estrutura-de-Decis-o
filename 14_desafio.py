__autor__ = "Jivaldo Da Cruz"

lista = []

for x in range(3):
    lista.append(float(input(f"Informe {x + 1}º lado do triangolo: ")))

cont = 0

if((lista[0] + lista[1]) > lista[2] or (lista[1] + lista[2]) > lista[0] or (lista[0] + lista[2]) > lista[1]):
    for z in lista:
        if(lista[0] == z):
            cont += 1
    if(cont == 3):
        print("Triângulo Equilátero")
    elif(cont == 2):
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escoleno")
else:
    print("Não é um triângulo.")
