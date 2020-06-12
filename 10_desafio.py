__autor__ = "Jivaldo Da Cruz"

listaTempo = ["Bom Dia!", "Boa Tarde!", "Boa Noite!"]

print("M-matutino ou V-Vespertino ou N- Noturno")
op = input("Informe em que turno estudas?[M, V ou N]: ")

if(op.lower() == "m"):
    print(listaTempo[0])
elif(op.lower() == "v"):
    print(listaTempo[1])
elif(op.lower() == "n"):
    print(listaTempo[2])
else:
    print("Valor Inválido!")
