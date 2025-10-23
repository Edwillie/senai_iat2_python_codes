import numpy as np

a = np.array([1,2,3,4])
b = np.array([10,20,30,40])

print("====== Operações =======")
print("a + b = ", a + b)
print("a * b = ", a * b)
print("a ** 2 = ", a ** 2)
print("a * 10 = ", a ** 10)

print("====== Elementos =======")
print("Primeiro: ", a[0])
print("Ultimo: ", a[-1])
print("Indice 1 ao 3: ", a[1:4])

print("====== Matriz =======")
matriz = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("Matriz \n", matriz)
print("Elemento [1,2] ", matriz[1,2])
print("Segunda Linha ", matriz[1:2])
print("Terceira Coluna ", matriz[:,2])
