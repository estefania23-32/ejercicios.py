# Nivel Básico
"""Saludo personalizado
 Crea una función que reciba un nombre y muestre un saludo personalizado."""""
def saludar(nombre):
 print("bienvenido de nuevo",nombre,"es un placer verte")
saludar("pedro")
saludar("maria")
saludar("jose")
saludar("lucas")

print("*" * 38)
#Suma de dos números
"Escribe una función que reciba dos números y devuelva su suma."
def suma(a,b):
 resultado = a + b
 return resultado
print("el resultado es: ")
print(suma(79,4))
print(suma(4,7))
print(suma(8,9))
print(suma(2,3))

print("*" * 38)
#Número par o impar
#Crea una función que determine si un número es par o impar.
 
def par_impar(numero):
    return numero % 2 == 0
print(par_impar(6))
print(par_impar(7))
print(par_impar(4))
print(par_impar(3))

print("*" * 38)
#Mayoría de edad
#Escribe una función que reciba una edad y devuelva si es mayor o menor de edad 
def calculate_age(edad):
 if edad >= 18:
  print("mayor de edad")
 else:
     edad <= 17
     print("menor de edad")
calculate_age(16)

print("*" * 38)
#Conversor de temperatura
#Crea una función que convierta grados Celsius a Fahrenheit.
def celsius_fahrenheit(celsius):
  return (celsius * 1.8) + 32
print(celsius_fahrenheit(18))

print("*" * 38)

#Área de un triángulo
#Escribe una función que devuelva el área de un triángulo dado su base y altura.
def area_triangulo(base,altura):
 return (base * altura) / 2
print("el area del triangulo es:")
print(area_triangulo(23,15))

print("*" * 38)

#Mayor de una lista
#Crea una función que reciba una lista de números y devuelva el mayor.
def num_mayor(lista):
    return max(lista)
numeros=[5,16,14,47,98,234,765,95,12222]
mayor=num_mayor(numeros)
print(f"el numero mayor es:{mayor}")

print("*" * 38)

#Contar letras
#Escribe una función que cuente cuántas veces aparece una letra en una palabra.
def contador(palabra,letra):
    return palabra.lower().count(letra.lower())
resultado =contador("esternocleidomastoideo","e")
print("la letra se repite:")
print(resultado)


print("*" * 38)


"Nivel Intermedio"
#Filtrar pares
#Crea una función que reciba una lista de números y devuelva solo los pares.}
def obtener_pares(lista):
    return [numero for numero in lista if numero % 2 == 0]
numeros=[1,3,5,4,23,24,56,76,42,49,75,34,22,33,44]
pares = obtener_pares(numeros)
print(f"numeros pares:{pares}")
    
print("*" * 38)
#Palíndromo
#Escribe una función que determine si un texto es un palíndromo.
def palindromo(texto):
     texto=texto.lower().replace(" ","")
     return texto == texto[::-1]
print(palindromo("anita lava la tina"))
print(palindromo("reconocer"))
print(palindromo("hola mundo"))
 
print("*" * 38)
#Factorial
#Crea una función que calcule el factorial de un número entero positivo.

#Eliminar duplicados
#Escribe una función que reciba una lista y devuelva una nueva sin elementos repetidos.

#FizzBuzz
#Crea una función que reciba un número y devuelva "Fizz", "Buzz" o "FizzBuzz" según las reglas del juego.
def fizzBuzz():
    numero = int(input("Ingresa un número a válida: "))
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)

fizzBuzz()
#Contar vocales
#Escribe una función que reciba una cadena y devuelva la cantidad de vocales.

#Invertir texto
#Crea una función que invierta una cadena de texto.
