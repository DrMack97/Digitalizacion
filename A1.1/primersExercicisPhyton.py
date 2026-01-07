
# ejercicio calculadora sencilla 

print("introduzca dos numeros:")

a= int(input("primer numero: "))
b= int(input("segundo numero: "))

suma = a + b
resta = a - b
multiplicacion = a * b
division = a/b

if b != 0:
    print(f"division:  {division}")
else:
    print("no se puede dividir por 0")

print(f"suma: {suma}")
print(f"resta: {resta}")
print(f"multiplicacion: {multiplicacion}")
print(f"division: " ,{division}) #puede ser , o ir dentro de las comillas 