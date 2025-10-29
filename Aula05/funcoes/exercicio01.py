lValor = ""
lLista = []

def soma(pLista):
    return sum(pLista)

def media(pLista):
    return sum(pLista) / len(pLista)

while lValor.upper() != "Q":
    lValor = input("Digite um valor ou 'Q' para sair:")
    try:
        lLista.append(int(lValor))
    except:
        if lValor.upper() != "Q":
            print("Digite um número ou 'Q' para sair!")

operacao = input("Qual Operacao deseja fazer: 1-Soma / 2-Media: ")

if (operacao.upper() == '1') or (operacao.upper() == 'Soma') or (operacao.upper() == '1-Soma'):
    print("Seu total é: ", soma(lLista))
elif (operacao.upper() == '2') or (operacao.upper() == 'Media') or (operacao.upper() == '2-Media'):
    print("Seu total é: ", media(lLista))
else:
    print("A operação não é valida!")    