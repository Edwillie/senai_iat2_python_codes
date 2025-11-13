#Desafio 05
print("Você está respondendo por conta própria ou por terceiros? ")
print("Se for por conta própria, digite: PROPRIO")
print("Se for por terceiros, digire: OUTROS")
resposta = input("> ")
entrada = True

if resposta.upper() == "PROPRIO":
    pessoa = "Você"
    idade = input("Digite sua idade: ")

elif resposta.upper() == "OUTROS":
    pessoa = input("A pessoa é alfabetizada? (Sim / Não): ")
    idade = input("Digite a idade da pessoa: ")

else:
    entrada = False
    print("Entradas inválidas")

if entrada:
    if pessoa == "Você":
        print("Você é alfabetizado e tem: ", idade, "anos")
    else:
        if pessoa == "Sim":
            print("A pessoa consultada é alfabetizada e tem: ", idade, "anos")
        else:
            print("A pessoa consultada NÃO é alfabetizada e tem: ", idade, "anos")    

#Desafio 03
if int(idade) <= 18:
    autorizacaoParental = True if input("Esse menor tem autorizacao dos pais? (Sim/Não) ").upper() == "SIM" else False

    print("A pessoa pesquisada", "" if autorizacaoParental else "NÃO", "possui autorização dos pais")

else:
    print("A pessoa pesquisada não requer autorização dos pais")