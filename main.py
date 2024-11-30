# EJERCICIOS 
# -----------------------

# Ejercicio 1.1: Crea 2 variables para imprimir en la consola
print("Ejercicio 1.1:")
var1 = "Hola"
var2 = "Mundo"
print(var1)
print(var2)
print()

# Ejercicio 1.2: Crea otras 2 variables de texto y concatenalas en una sola impresión
print("Ejercicio 1.2:")
texto1 = "Python me"
texto2 = "encanta"
print(texto1 + " " + texto2)
print()

# Ejercicio 1.3: Crea 2 variables, imprímelas, modifica el contenido de una y vuelve a imprimirla
print("Ejercicio 1.3:")
var_a = 10
var_b = 20
print("Valores iniciales:", var_a, var_b)
var_a = 30
print("Valores modificados:", var_a, var_b)
print()

# Ejercicio 2.1: Verifica si un valor ingresado es par o impar
print("Ejercicio 2.1:")
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
print()

# Ejercicio 2.2: Verifica si un valor es mayor o menor a 20
print("Ejercicio 2.2:")
valor = int(input("Ingresa un valor: "))
if valor > 20:
    print(f"El valor {valor} es mayor que 20.")
else:
    print(f"El valor {valor} es menor o igual a 20.")
print()

# Ejercicio 2.3: Condición que evalúe 2 posibilidades
print("Ejercicio 2.3:")
edad = int(input("Ingresa tu edad: "))
if edad < 18:
    print("Eres menor de edad.")
elif edad >= 18:
    print("Eres mayor de edad.")
print()

# Ejercicio 3.1: Ciclo que escriba 5 veces "Python" en la consola
print("Ejercicio 3.1:")
for _ in range(5):
    print("Python")
print()

# Ejercicio 3.2: Ciclo para generar números del 1 a un valor ingresado
print("Ejercicio 3.2:")
limite = int(input("Ingresa un número: "))
for i in range(1, limite + 1):
    print(i, end=" ")
print("\n")

# Ejercicio 3.3: Ciclo que muestre números pares desde 0 hasta un valor ingresado
print("Ejercicio 3.3:")
maximo = int(input("Ingresa un número: "))
for i in range(0, maximo + 1, 2):
    print(i, end=" ")
print("\n")

# Ejercicio 4.1: Crea una lista, una tupla y un conjunto, e intenta acceder a sus datos
print("Ejercicio 4.1:")
lista = [1, 2, 3]
tupla = (4, 5, 6)
conjunto = {7, 8, 9}
print("Lista:", lista)
print("Tupla:", tupla)
print("Conjunto:", conjunto)
print()

# Ejercicio 4.2: Crea una lista y muestra valores específicos de ella
print("Ejercicio 4.2:")
nueva_lista = ["a", "b", "c", "d", "e"]
print("Primer elemento:", nueva_lista[0])
print("Último elemento:", nueva_lista[-1])
print("Sublista (2 al 4):", nueva_lista[1:4])
print()
