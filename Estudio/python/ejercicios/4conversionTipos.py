# la lectura por teclado almacena una cadena o string
# para almacenar en otro tipo de datos
# se requiere convertir los valores
cantidad=input("Ingrese un valor numerico ")

# print(f"{cantidad}/2={cantidad/2}")
# esta operación genera un error por la diferencia del tipo de datos
# para convertir una cadena en un entero
cantidad=int(cantidad)
print(f"{cantidad}/2={cantidad/2}")

# para  almacenar un valor decimal se utiliza la función float

# decimal=int(input("Ingrese un valor decimal"))
decimal=float(input("Ingrese un valor decimal "))
print(f"El valor decimal es {decimal}")


