from datetime import date

anoAtual = date.today().year
anoNasci = int(input("Entre com o ano de nascimento: "))
idade = anoAtual - anoNasci

print(f"Você tem {idade} anos")

if idade >= 16:
    print("Você pode votar!")
else:
    print("Você não pode votar!")