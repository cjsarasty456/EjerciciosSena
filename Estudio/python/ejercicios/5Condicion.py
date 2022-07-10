# Para realizar una condición en python se utiliza 
# los operadores lógicos
# == igual a en el que se compara si un valor es igual a otro
# >  Mayor que 
# >= Mayor o igual
# < Menor que
# <= Menor o igual

num=5

if num>0:
    print("El numero es positivo")
else:
    print("El numero es negativo")

if num%2==0:
    print("El numero es par")
else:
    print("El numero es impar")

edad=input("¿Cuantos años tiene? ")
if edad<18:
    print("Es menor de edad")
else:
    print("Es mayor de edad")