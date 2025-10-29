def fatorial(numero):
    if numero==0:
        return 1
    else:
        return numero * fatorial(numero-1)
    

n=5
calcular = fatorial(n)

print("O fatorial de", n , "é", calcular)