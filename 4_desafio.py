__autor__ = "Jivaldo Da Cruz"

consoantes = "b c d f g h j k l m n p q r s t v w x y z".split()
vogais = "a e i o u".split()

ins = input("Insira uma letra para saberes se é vogal ou consoante: ")

cont = 0#contador

while True:
    if(ins.lower() == consoantes[cont]):
        print("É uma consoantes.")
        break
    elif(ins.lower() == vogais[cont]):
        print("É um vogal.")
        break
    cont += 1
