def lista_alumnos_segura(lista):
    if not lista:  # CORREGIDO: "not lista" no "not_lista"
        return 0.0
    
    try:
        return sum(lista) / len(lista)
    except ZeroDivisionError:
        return 0.0
    except TypeError:
        # Elementos no numéricos - CORREGIDO: "lista" no "lists"
        numeros = [n for n in lista if isinstance(n, (int, float))]
        return sum(numeros) / len(numeros) if numeros else 0.0

notas2 = {
    'duver': [8, 9, 5],
    'vilma': [7, 4, 6],
    'daniela': [9, 5, 7],
    'richard': [7, 9, 6],
    'Noland': [0],
    'david': ['P', 'R', 0],  # Con letras
    'wilmar': []  # Lista vacía
}

for alumno2, lista in notas2.items():
    media = lista_alumnos_segura(lista)  # CORREGIDO: nombre de función
    print(f"{alumno2:10} > {media:6.2f}   (notas: {lista})")