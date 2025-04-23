#Crea una pequeña calculadora 
# que realice las operaciones básicas: suma, resta, multiplicación y división.
def suma(a, b):
    return a + b
          
def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Error: División por cero no permitida."
    else:
        return a / b
    

def calculadora():
    print("Bienvenido a la calculadora")
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    while True:
        try:
            operacion = int(input("Ingrese el número de la operación (1/2/3/4): "))
            if operacion in [1, 2, 3, 4]:
                break
            else:
                print("Operación no válida. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
    
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    if operacion == 1:
        resultado = suma(num1, num2)
        print(f"La suma de {num1} y {num2} es: {resultado}")
    elif operacion == 2:
        resultado = resta(num1, num2)
        print(f"La resta de {num1} y {num2} es: {resultado}")
    elif operacion == 3:
        resultado = multiplicacion(num1, num2)
        print(f"La multiplicación de {num1} y {num2} es: {resultado}")
    elif operacion == 4:
        resultado = division(num1, num2)
        print(f"La división de {num1} entre {num2} es: {resultado}")
    else:
        print("Operación no válida.")









if __name__ == "__main__":
    calculadora()   







