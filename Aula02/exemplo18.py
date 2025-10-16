import random

numero_secreto = random.randint(1,100)
tentativa = 1

while tentativa <= 3: 
    valor = int(input("Entre com um palpite: "))
    if valor == numero_secreto:
        print("Acerrrrrtou!")
        break
    else:
        if valor > numero_secreto:
            print("Ajuste para um valor maior que ", valor)
        else:
            print("Ajuste para um valor menor o", valor)

    tentativa += 1

if tentativa > 3:
    print("Errou!")
        