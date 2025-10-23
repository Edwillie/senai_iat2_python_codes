import numpy as np

arr1 = np.array([1,2,3,4,5])
print("Array 1D: ", arr1)

arr2 = np.array([[1,2,3], [4,5,6]])
print("Array 2D: ", arr2)

zero = np.zeros(10)
print("Zeros ", zero)

uns = np.ones((3,3))
print("Uns ", uns)

identidade = np.eye(3)
print("Identidade ", identidade)

intervalo = np.arange(0,10,2)
print("Intervalo ", intervalo)

linear = np.linspace(0, 1, 50)
print("Linear ", linear)