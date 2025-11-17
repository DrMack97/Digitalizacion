# (1) operaciones basicas con listas 
squares = [1, 4, 9, 16, 25] 
print(squares)

nombres = ['Ana', 'Luis', 'Carlos', 'Marta']

print(nombres[0])  # Acceder al primer elemento
print(nombres[3])  # Acceder al ultimo elemento

nombres[1] = 'maria'  # Cambiar el segundo elemento
nombres[2] = 'lucia'  # Cambiar el tercer elemento
print(nombres)

colores = [rojo, verde, azul, amarillo]
print(colores)
colores.append('naranja') # Añadir un nuevo color al final
colores.pop(4) #eliminar el ultimo color
print(colores)


long = len(squares)
print("La longitud de la lista squares es:", long)

long_nombres = len(nombres)
print("La longitud de la lista nombres es:", long_nombres)