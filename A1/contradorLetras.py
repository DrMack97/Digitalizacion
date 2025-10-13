s= "hello"          # establecr palabra 
lletra = "l"        # indicar letra para contar
cont=0              # inicializar contador
for x in s:         # recorre cada letra de la cadena
    if x == lletra: # si x es igual a letra (indicada ) contador suma + 1
        cont+=1 
        
print("la cadena ",s," tiene ", cont, " letras ", lletra) # imprime la cadena, la letra y el contador

textdna ="atggatcattta"
letra = "t" 
cont=0                  # inicializar contador

for x in textdna:
    if x == letra:
        cont+=1
print("la cadena ",textdna," tiene ", cont, " letra ",letra)