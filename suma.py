# suma de dos números
while True:

        print("Bienvenido usuario")
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        suma = num1 + num2  
        print("La suma de " + str(num1) + " y " + str(num2) + " es: " + str(suma))
        continuar = input("¿Desea realizar otra suma? (s/n): ")
        if continuar.lower() != 's':  
            break