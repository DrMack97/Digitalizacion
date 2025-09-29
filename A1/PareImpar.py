print("ingrese un numero: ")
numero = input()
if(numero.isnumeric()):
    numero=int(numero)
    print("no es un numero")
    reste = int(numero) % 2
    if (reste == 0):
        print(f"el numero {numero} es par")
    else:
        print(f"el numero {numero} es impar")
else:
    print("no es un numero")
