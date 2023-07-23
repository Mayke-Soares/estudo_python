#Variável (r) recebendo valor de (S)
r = "S"
#Equando (r) for igual a ("S")
while r == "S":
#inserindo valor e pedindo solicitação de continuação.
    n = int(input("Digite um valor: "))
    r = str(input("Quer continuar? [S/N]")).upper()
print("Fim")
