def ordenaLista(pLista):
    trocou = True
    print("Antes")
    print(pLista)

    while trocou:
        trocou = False
        i = 0

        while i+1 <= len(pLista)-1:
            if pLista[i] > pLista[i+1]:
                trocou = True
                pLista[i] , pLista[i+1] = pLista[i+1] , pLista[i]
            i += 1        
        
    print("depois")
    print(pLista)

    return pLista

lValor = ""
lLista = []

while lValor.upper() != "Q":
    lValor = input("Digite um valor ou 'Q' para sair:")
    try:
        lLista.append(int(lValor))
    except:
        if lValor.upper() != "Q":
            print("Digite um número ou 'Q' para sair!")

if len(lLista) > 1:
    ordenaLista(lLista)
else:
    print("Não há elementos suficientes para ordenar")    