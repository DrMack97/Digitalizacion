#Ejercicio 1
Saludo = "hola mundo"
nombre = "david"

print(Saludo, "dice",nombre)

#Ejercicio 2 edad

Nacimento = 1997
fechaActual = 2025

edad = fechaActual - Nacimento

print("tienes",[edad],"años")

#Ejercicio 3 

nombre = input("com et dius? ")
lugar = input("on vius? ")

print("hola", nombre ,"de", lugar)

#Ejercicio 4  if/else

edad= int(input("quants anys tens  ")) ## al uar numero no olvidar definir de esta manera -> int(input) <-

if edad < 18: print("eres menor de edad")
else: print("eres mayor de edad")

#Ejercicio 5  for "lista"

listaDeCompra = ["manzanas"],["pan"],["aceite"],["leche"]

for producto in listaDeCompra: print("necesito comprar:" , producto) ## poner for ->"nombre lista" -> in "indicar lugar de la lista".