palavra = input("Entre com uma palavra: ")

novaPalavra = ""
for letra in palavra:
    if letra in "AÁÀÂÃaáàãâEÉÈÊeéèêIÍÌÎiíìîOÓÒÔÕoóòõôUÚÙÛuúùû":
        continue
    else:
        novaPalavra += letra

print(novaPalavra)