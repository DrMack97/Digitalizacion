# Crea una lista con 5 números enteros y muéstrala por pantalla.

lista_ent = [13, 15, 14, 25, 32]
print("Lista de números enteros:", lista_ent)

# Crea una lista de nombres, muestra el primer y último elemento.

lista_nombres = ["Ana", "Luis", "Carlos", "Marta", "Sofía"]
print("Primer nombre:", lista_nombres[0])
print("Último nombre:", lista_nombres[-1])

# Añade un elemento nuevo al final de una lista y elimina el primero.

lista_colores = ["rojo", "verde", "azul"]
lista_colores.append("amarillo")
print(lista_colores)

lista_colores.pop(0)

print(lista_colores)

# Muestra cuántos elementos tienen las listas que has creado

print("cantidad de elementos lista num ", len(lista_ent))
print("cantidad de elementos lista nombres ", len(lista_nombres))
print("cantidad de elementos lista colores ", len(lista_colores))
