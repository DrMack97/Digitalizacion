a=input("ingrese numero 1: ")
b=input("ingrese numero 2: ")
print(" tipo de dato:" , type(a))
if(a.isnumeric() and b.isnumeric):
    c = int(a) + int(b)
    print(f"la suma de {a} + {b} = {c}")
    d = int(a) - int(b)
    print(f"la resta de {a} - {b} = {d}")
    f = int (a) * int (b)
    print(f"la multiplicacion de {a} * {b} = {f}")
    g = int(a) / int(b)
    print(f"la division de {a} / {b} = {g}")
    e = int(a) % int(b)
    print(f"el modulo de {a} % {b} = {e}")
else:
    print("Error: debe ingresar numeros")
    

print("FINAL")