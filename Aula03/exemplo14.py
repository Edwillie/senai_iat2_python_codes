numeros=[10,20,25,11,40]

maior = 0
soma = 0
for numero in numeros:
    soma += numero
    if numero > maior:
        maior = numero

print("maior", maior)
print("soma", soma)

print("="*10)

soma = sum(numeros)
minimo = min(numeros)
maximo = max(numeros)
ordenado = sorted(numeros)
numeros.sort()

print("Soma: ", soma)
print("Minimo: ", minimo)
print("Maximo: ", maximo)
print("Ordenados: ", ordenado)
print("Lista Ordenada: ", numeros)

numeros.sort(reverse=True)
print("Lista Reversa: ", numeros)