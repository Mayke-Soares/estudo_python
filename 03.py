#LAÇO DE REPETIÇÃO

#(i) númeiro inicial do programa
i = int(input("Indice"))
#(f) Determinará o útimo número
f = int(input("Fim"))
#(p) Determinará a quantidade de números pulados
p = int(input("Passo"))

#Para dentro de (c) na distância de: 
for c in range(i, f, p):
    print(c)
print("Fin")
