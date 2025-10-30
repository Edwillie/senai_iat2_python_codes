def parImpar(n):
    if (n % 2 == 0):
        return "Par"
    else:
        return "Impar"
    
print("Seu numero é:", parImpar(int(input("Entre com o valor: "))))