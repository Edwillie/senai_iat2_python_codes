print("===== CALCULADORA IMC =====")
peso = float(input("Informe seu peso em kg: "))
altura = float(input("Informe sua altura em m (exemplo: 1.75): "))

vimc = peso / (altura**2)

print("Seu IMC é: ", round(vimc, 2))

if (vimc < 18.5):
    print("Abaixo do peso")
elif (vimc < 25):
    print("Peso normal")
elif (vimc < 30):
    print("Sobrepeso")
else:
    print("Obesidade")        