x = int(input("Digite valor x: "))
y = int(input("Digite valor y: "))
z = int(input("Digite valor z: "))

if (x > y) and (x > z):
    resultado = "x é o maior"
elif (y > x) and (y > z):
    resultado = "y é o maior"    
elif (z > x) and (z > y):
    resultado = "y é o maior"
else:
    resultado = "Há números iguais"

print(resultado)            