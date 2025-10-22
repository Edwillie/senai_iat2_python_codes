tentativas = 0

while tentativas < 3:
    senha = input("Digite a senha: ")
    if senha == "senha123":
        print("Acesso Concedido!")
        break
    else:
        tentativas += 1
        print("Senha Incorreta. Tente novamente!")
        print(f"Restam {3 - tentativas} tentativas")
        
else:
    print("Você excedeu o numero de tentativas!")