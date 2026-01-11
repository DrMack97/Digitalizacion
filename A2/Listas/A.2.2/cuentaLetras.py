# 2.5. Comptar aparicions de lletres

palabra = input("introduce una palabra: ").lower()

contar_letras = {}

for letra in palabra:
    if letra in contar_letras:
        contar_letras[letra] += 1
    else:
        contar_letras[letra] = 1
print(f"\nConteo de letras en '{palabra}':")
print(f"resultado> {contar_letras}")

# 2.6 fusionar dos diccionario 

preus1 = {'pa': 1.2, 'llet': 0.9}
preus2 = {'formatge': 2.5, 'pa': 1.1}
preus3 = preus1 | preus2
print("")
print(preus3)