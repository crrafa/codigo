def mayor(x,y):
    if x>y:
        return x
    return y

a=17
b=18
c=14
d=25

#esta funcion utilizar recursividad
maximo = mayor(mayor(a,b), mayor(c,d))
print("Hola mundo")
print ("El numero maximo es",maximo)

print ("final de la linea")
    