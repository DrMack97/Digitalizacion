preus = {'motxilla': 45, 'llapis': 1, 'calculadora': 25, 'libreta': 15, 'pc':650}

productos_caros = {}

for producto , preus in preus.items():
    if preus > 20:
        productos_caros[producto] = preus
    
print("productos caros")
print(productos_caros)
    
