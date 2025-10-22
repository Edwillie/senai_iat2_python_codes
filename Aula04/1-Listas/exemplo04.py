numeros=[11,7,2,3,1]
trocou = True

print("Antes")
print(numeros)

while trocou:
    trocou = False
    i = 0

    while i+1 <= len(numeros)-1:
        if numeros[i] > numeros[i+1]:
            trocou = True
            numeros[i] , numeros[i+1] = numeros[i+1] , numeros[i]
        i += 1        
        
print("depois")
print(numeros)
