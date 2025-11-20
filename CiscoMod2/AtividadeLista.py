lstNumeros = []

while True:
    try:
        numero=int(input("Digite um número ou QQ outra tecla para sair:"))
        print('Sua lista contém', len(lstNumeros)+1,'elementos')
    except:
        break
    else:
        lstNumeros.append(numero)
    finally:
        print('*'*20)

if len(lstNumeros)>0:
    print('Sua lista digitada foi: ', lstNumeros)

    print('> Ex 1 < Números pares:', sorted([num for num in lstNumeros if num % 2==0]))
    print('> Ex 2 < O menor número é:', min(lstNumeros), 'e o maior numero é:', max(lstNumeros))
    print('> Ex 3 < A média é:', sum(lstNumeros) / len(lstNumeros))
    print('> Ex 4 < A média é:', list(set(lstNumeros)))

        