numeros=[11,7,2,3,1]

print("Antes")
print(numeros)

numeros[0], numeros[4] = numeros[4], numeros[0]

print("passo 1")
print(numeros)

numeros[1], numeros[3] = numeros[3], numeros[1]

print("passo 2")
print(numeros)
