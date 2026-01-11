# 2.10. Freqüència de paraules en una frase

frase = "el gat menja el peix"

frase_espacios = frase.split()
contador = {}

for palabra in frase_espacios:
    if palabra in contador:
        contador[palabra] += -1
    else:
        contador[palabra] = 1

print ("\nfrecuencia de palabras ")
print(contador)