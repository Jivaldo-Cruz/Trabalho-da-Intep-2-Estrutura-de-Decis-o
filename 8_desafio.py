__autor__ = "Jivaldo Da Cruz"

lista = []
produtos = {"Lenovo": 700, "MacBook": 1000, "Huawei": 450, "Samsung": 350, "PS5": 600}

print("Nome e Preço dos Produtos")
for x, y in produtos.items():
    print(x,":", y,"€ ")

for z in range(3):
    buy = input(f"Insira nome de {z + 1} produto: ")
    for i, n in produtos.items():
        if(buy.lower() == i.lower()):
            lista.append(n)
print(f"O produto mais barato a ser comprado é de -> {min(lista)}€")
