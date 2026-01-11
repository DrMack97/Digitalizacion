palabras =["biodon", "datos", "phyton","biodon","python","python"]
frecuencia = {}
## contar el numero de veces que aparece una palabra en el errays
for palabras in palabras:
    frecuencia[palabras ] =frecuencia.get(palabras, 0 )+1
print(frecuencia)

# 2 ejercicio 

'''2.1. Crear i accedir a valors
Crea un diccionari anomenat cotxe amb les claus "marca", "model" i "any".
Mostra per pantalla el valor associat a la clau "marca".'''

coche = {"marca": "mercedez",
        "model": "A200",
        "any": "2014"
                        }

## Añadir
coche["color"] = "verde"

#eliminar 

del coche["any"]

print(coche)

# iterar por claves y valores 

capital_pais= { "espanya ": " madrid",
                "colombia ":" bogota",
                "vnzla ": " caracas " }

for pais in capital_pais:
    print(f"la capital de {pais} es {capital_pais[pais]}")

# con get capital_pais

colombia = capital_pais.get("colombia "," no existe")
print(colombia)




