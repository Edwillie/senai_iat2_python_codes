import numpy as np

print("===== Funcoes ======")
dados = np.array([1,2,3,4,5,6,7,8,9,10])
print("Dados ", dados)

print("===== Estatisticas ======")
print("Soma ", np.sum(dados))
print("Media ", np.mean(dados))
print("Mediana ", np.median(dados))
print("Desv Pad ", np.std(dados))
print("Minimo ", np.min(dados))
print("Maximo ", np.max(dados))