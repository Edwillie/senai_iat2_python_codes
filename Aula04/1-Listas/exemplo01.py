lista_duplicados = [1,2,3,3,2,1,4,5,6,6,5,4,7,8,9,9,8,7]
lista_limpa = []

print('Antes:')
print('Lista Antiga = ', lista_duplicados)
print('Lista Limpa = ', lista_limpa)

while lista_duplicados:
    elemento = lista_duplicados.pop(0)

    if elemento not in lista_limpa:
        lista_limpa.append(elemento)

print('Depois:')
print('Lista Antiga = ', lista_duplicados)
print('Lista Limpa = ', lista_limpa)