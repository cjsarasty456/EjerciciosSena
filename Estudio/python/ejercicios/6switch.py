def uno():
    print("opción uno")
def dos():
    print("opción dos")
def tres():
    print("opción tres")
def cuatro():
    print("opción cuatro")

# El switch es una estructura de control
# Que permite tomar diferentes caminos
# Según el valor de una variable,
# Similar a varias condiciones anidadas

print("1 para la opción uno")
print("2 para la opción dos")
print("3 para la opción tres")
print("4 para la opción cuatro")
opcion=int(input("Ingrese su opción deseada "))
print("Con condicionales anidadas")
if opcion==1:
    print("Opción uno selecionada")
elif opcion==2:
    print("Opción dos selecionada")
elif opcion==3:
    print("Opción tres selecionada")
elif opcion==4:
    print("Opción cuatro selecionada")
else:
    print("Opción no valida")

switcher={
    1:uno,
    2:dos,
    3:tres,
    4:cuatro
}
# simulador swicth
print("opción switch simulada")
func=switcher[opcion]
func()