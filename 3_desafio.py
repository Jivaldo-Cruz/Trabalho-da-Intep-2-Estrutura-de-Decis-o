__autor__ = "Jivaldo Da Cruz"

sexo = input("Insira o sexo feminino[F] ou masculino[M]: ")

if(sexo.lower() == "m"):
    print("Masculino")
elif(sexo.lower() == "f"):
    print("Feminino")
else:
    print("Tens que digitar entre F ou M")
