#Solicita un número y muestra si es positivo, negativo o igual a cero.

input = int(input("Ingrese un número: "))
if input > 0:
    print("El número es positivo.")
elif input < 0:
    print("El número es negativo.")
else:
    print("El número es igual a cero.")
    