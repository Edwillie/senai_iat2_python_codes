numero = int(input("Entre com um número maior que 2: "))

if numero <= 2:
    print("Você deveria ter informado um número maior que 2")
else:
    for i in range(2, numero):
        if numero % i == 0:
            print(numero, "não é primo.")
            break
    else:
        print(numero, "é um numero primo")