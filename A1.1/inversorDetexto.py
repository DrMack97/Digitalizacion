 #10 inversor 
#usar ejemploSTR[::-1]
palabra= input("revertidor de palabras ")

invertida = palabra[::-1]
print(f"palabra invertida {invertida}")

# 11 contador de letras y posicion en una cadena
#usar .count
print(" ")
textdna =  "atggatcattta"
cantidad_a = textdna.count('a')
print(textdna)
print(f"Cantidad a 'A' : {cantidad_a}")
print(" ")

# 12 misma posicion 

text =  "Hello World"
text2 = "Hola mon!!!" 
print(text )
print(text2)

caracteres_misma_posicion = []

longitud_minima = min(len(text), len(text2)) #tomar la longitud mas corta 

for i in range(longitud_minima):
    if text[i] == text2[i]:
        caracteres_misma_posicion.append(text[i])
print(f"Caracteres iguales {caracteres_misma_posicion}")

# 13 convertir en mayuscula y miniscula 

text = "Hello World"
print(text)

print("miniscula: ", text.lower())
print("mayuscula :", text.upper())

# 14 iterar una palabra 
#o reverso de izquierda a derecha
palabra = input("escribe una palabra: ")
invertida = ""

for letra in palabra:
    invertida = letra + invertida
print(f"Palabra invertida: {invertida}")