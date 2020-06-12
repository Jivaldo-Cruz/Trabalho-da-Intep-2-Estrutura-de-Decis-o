__autor__ = "Jivaldo Da Cruz"

valor = int(input("Insira um ano do calendário: "))

if(valor%400 == 0 or valor%100 != 0):
    print(f"{valor} é um ano bissexto")
else:
    print(f"{valor} não é um ano bissexto")
