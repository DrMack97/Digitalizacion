#crear diccionario con clave mayor 

alumne ={
    "nom":"mario",
    "edad":21,
    "curso":"informatica"
}

## aceder a una clave mayor por su nombre

print(alumne["nom"])

print(alumne["edad"])

print(alumne["curso"])

#elimnar o modificar


alumne["edad"] = 28
print(alumne["edad"])

## añadir
alumne["nota"] = 9.5

#eliminar
del alumne["curso"]

print(alumne)

#recorrer claves el valor o ambas a la vez

for clau, valor in alumne.items():
    print(f"{clau}: {valor}")

#comprovar si existe

if "edad" in alumne:
    print("existe")

#usar GET

nom = alumne.get("nom", "desconectado")
print(nom) #maria 

