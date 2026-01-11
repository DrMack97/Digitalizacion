alumnos = {
    'Marta': {'edad': 18, 'nota_final': 8.5},
    'Juan': {'edad': 19, 'nota_final': 6.7},
    'Ana': {'edad': 17, 'nota_final': 9.2},
    'Pablo': {'edad': 18, 'nota_final': 7.8},
    'Sofía': {'edad': 19, 'nota_final': 9.5}
}
# encontrar alumno con la mejor nota 

mejor_nota = -1 #inicializar con valor bajo
mejor_alumno = ""

for nombre, datos in alumnos.items():
        if datos ['nota_final'] > mejor_nota:
            mejor_nota = datos['nota_final']
            mejor_alumno = nombre

# resultado
print(f"El alumno con mejor nota es: {mejor_alumno}")
print(f"Nota: {mejor_nota}")
print(f"Edad: {alumnos[mejor_alumno]['edad']} años")