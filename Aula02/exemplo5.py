nota1 = float(input("Entre com a nota 1: "))
nota2 = float(input("Entre com a nota 2: "))
nota3 = float(input("Entre com a nota 3: "))
nota4 = float(input("Entre com a nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"Aluno com média {media}.")

if (media >= 7):
    print("Aluno aprovado!")
elif (media >= 5):
    print("Aluno em recuperação!")
else:
    print("Aluno reprovado!")