__autor__ = "Jivaldo Da Cruz"

comp = 0
print("Digite 3 números para saber qual é o maior")
for x in range(3):
    op = float(input(f"Informe {x + 1}º número: "))
    if(comp < op):
        comp = op

print(f"O maior número é {comp}")
