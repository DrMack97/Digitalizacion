s= "Helljkljkljkljkljkljkljkl"
c= "Hola mon!!!"
ls=len(s)
lc=len(c)
lenmin=0
if ls < lc:
    lenmin=ls
else:
    lenmin = lc
cont=0 
for x in range(lenmin):
    print(x, s[x],c[x])
    if s[x]==c[x]:
        cont+=1
    
        
print("la cadena", s, "tiene ", cont, "letras similares con respecto a",c )