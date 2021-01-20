def mayor(x,y):
    if x>y:
        return x
    return y

a=17
b=18
c=14
d=25

#esta funcion utilizar recursividad
print("Hola el numero mayor es")
maximo = mayor(mayor(a,b), mayor(c,d))


#se eliminara este comentario
    # Esto es para comprobar la sobreescritura de git