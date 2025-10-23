import time
import numpy as np

lista = list(range(10))
print(lista)

tamanho = 100_000_000
lista_a = list(range(tamanho))
lista_b = list(range(tamanho))

print ("*"*20," Sem Numpy ","*"*20)
resultado = []

startTime = time.time()
for i in range(tamanho):
    resultado.append(lista_a[i] + lista_b[i])

endTime = time.time()

print("Tempo do loop: ", (endTime - startTime), " segundos")

print ("*"*20," Com Numpy ","*"*20)
startTime = time.time()
resultado = np.array(lista_a[i]) + np.array(lista_b[i])

endTime = time.time()
print("Tempo do Numpy: ", (endTime - startTime), " segundos")
