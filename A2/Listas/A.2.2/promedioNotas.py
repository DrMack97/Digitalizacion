# Diccionario de notas 

notas = { 'Ana':[8,9,7], 'Paul':[5,6,6] }

print("PROMEDIO")
print("="*25)

for alumno, lista_notas in notas.items():
    media = sum(lista_notas) / len(lista_notas)
    print(f"{alumno} > {media:.2f}")


# mismo ejercio mas correccion de errores
print("\n"+"="*50+"\n")
# si la lista esta vacia