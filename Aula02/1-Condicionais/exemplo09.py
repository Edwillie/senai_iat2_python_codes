idade = int(input("Digite sua idade: "))
dinheiro = float(input("Quanto dinheiro você tem? "))
carteira = input("Você tem carteira (s/n)? ")

if (idade >= 18 and dinheiro >= 50) or (carteira == "s"):
    print("Você pode alugar um carro")
else:
    print("Você não pode alugar um carro")    