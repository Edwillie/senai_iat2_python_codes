numero = input("Informe PAR ou IMPAR: ").upper()

for i in range(0, 100):
    if (i % 2 == 0) and (numero == "PAR"):
        print(f"Modulo de {i} é {i % 2}, por isso é {numero}")
    elif (i % 2 != 0) and (numero == "IMPAR"):
        print(f"Modulo de {i} é {i % 2}, por isso é {numero}")   