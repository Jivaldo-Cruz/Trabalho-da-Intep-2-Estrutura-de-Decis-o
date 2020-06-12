__autor__ = "Jivaldo Da Cruz"

dic = {1: "Domingo", 2: "Segunda-Feira", 3: "Terça-Feira", 4: "Quarta-Feira", 5: "Quinta-Feira", 6: "Sexta-Feira", 7: "Sábado"}

op = int(input("Qual dia de semana queres?: "))

for x,z in dic.items():
    if(op == x):
        print(z)
    if(op < 1 or op > len(dic)):
        print("Valor Inválido!")
        break
