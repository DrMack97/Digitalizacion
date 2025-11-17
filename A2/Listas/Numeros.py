#contar aparaciones 

list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]

apariciones = list_num.count(5)
print("El numero 5 aparece", apariciones, "veces en la lista.")

# suma de elementos
list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]

suma = sum(list_num)
print("La suma de los elementos de la lista es:", suma)

# encontrar el valor maximo y minimo
list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]

maximo = max(list_num)
minimo = min(list_num)
print("El valor maximo en la lista es:", maximo)
print("El valor minimo en la lista es:", minimo)

# invertir la lista
list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]
list_num.reverse()
print("La lista invertida es:", list_num)

# concatenar dos listas
list_num1 = [2, 7, 4, 5, 1]
list_num2 = [8, 3, 9, 6, 10]
lista_concatenada = list_num1 + list_num2
print("La lista concatenada es:", lista_concatenada)

# verificar duplicados en la lista y contar duplicados
list_num3 = [6,9,6,9]
print("Lista original:", list_num3)
duplicados = set()
for num in list_num3:
    if list_num3.count(num) > 1:
        duplicados.add(num)
print("Numeros duplicados en la lista:", duplicados)
for num in duplicados:
    print(f"El numero {num} aparece {list_num3.count(num)} veces.")
    
# comprobar si un elemento existe en la lista
# Pregunta al usuario un número y comprueba si está dentro de una lista.

list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
num_us = int(input("introduce un numero "))
if num_us in list_num:
    print(f"El numero {num_us} existe en la lista.")
else:
    print(f"El numero {num_us} no existe en la lista.")

# Ordena una lista de números de menor a mayor.
list_num4 = [4,7,2,9,5,6]
sorted_list_acent = sorted(list_num4)
print("Lista ordenada de menor a mayor:", sorted_list_acent)

# Ordena una lista de números de mayor a menor.
list_num4 = [4,7,2,9,5,6]
sorted_list_desc = sorted(list_num4, reverse=True)
print("Lista ordenada de mayor a menor:", sorted_list_desc)

#Implementa amb l’algoritme d’ordenació “Selection Sort”
-----------------------------------------------------

#Implementa con el algoritmo de ordenación “Insertion Sort"
------------------------------------------------------



        