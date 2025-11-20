try:
    numero=int(input("Entre com um número: "))
    x=2/numero
except ZeroDivisionError as ze:
    print("Erro de divisão")
except:
    print("outro erro!")    
else:
    print(x)
finally:
    print("Passo por aqui, de qualquer forma")    