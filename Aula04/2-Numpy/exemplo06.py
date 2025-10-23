import numpy as np

notas_p1 = [7.5, 8.0, 6.5, 9.0, 5.5]
notas_p2 = [8.0, 7.0, 8.5, 7.5, 6.0]

print ("*"*20," Sem Numpy ","*"*20)
notas_finais = []

for i in range(len(notas_p1)):
    soma = notas_p1[i] + notas_p2[i]
    notas_finais.append(soma)

print("resultado: ", notas_finais, " - ", type(notas_finais))

print ("*"*20," Com Numpy ","*"*20)
arr_p1 = np.array(notas_p1)
arr_p2 = np.array(notas_p2)

notas_finais = arr_p1 + arr_p2
print("resultado: ", notas_finais, " - ", type(notas_finais))