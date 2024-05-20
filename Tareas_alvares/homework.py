# ejercicio 1 
# > Escribir un programa para una empresa que tiene salas de juegos para todas las edades
# y quiere calcular de forma automatica el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
# Si el cliente es menor de 4 puede entrar gratis, si tiene entre 4 y 18 debe pagar 5 soles, y 
# si es mayor de 18 deberá pagar 10 soles.
edad=int(input("ingrese su edad: "))
if edad < 4:
    print("puede ingresar gratis")
elif 4<= edad <=18:
    print("debe pagar 5 soles")
else:
    print("debe pagar un monto de 10 soles")

## Ejercicio 2:
# > Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces
palabra = input("Ingresa una palabra: ")
for _ in range(10):
    print(palabra)

## Ejercicio 3: 
#  > Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
# todos los números impares desde 1 hasta ese número separados por comas.
numero = int(input("Ingrese un número entero positivo: "))
print("Números desde 1 hasta", numero, ":")
for i in range(1, numero + 1):
    print(i, end=" ")

## Ejercicio 4: 
# > Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10. 
for i in range(1, 11):
    print(f"Tabla de multiplicar del {i}:")
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
    print()



 ## Ejercicio 5: 
# > Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una
# a una las letras de la palabra introducida empezando por la última.
palabra = input("Ingresa una palabra: ")
for letra in reversed(palabra):
    print(letra)


## Ejercicio 6: 
# > Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
# rectángulo como el de la imagen adjunta. 
# 1
# 31
# 531
# 7531
# 97531
numero = int(input("Ingrese un número entero: "))
for i in range(1, numero + 1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()
    


## Ejercicio 7:
# > Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
# pantalla el número de veces que aparece la letra en la frase.
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
contador = frase.count(letra)
print(f"La letra '{letra}' aparece {contador} veces en la frase.")


## Ejercicio 8:
# > Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las 
# letras de la palabra introducida empezando por la última.
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
contador = frase.count(letra)
print(f"La letra '{letra}' aparece {contador} veces en la frase.")


## Ejercicio 9:
# > Escriba un programa que pregunte cuántos números se van a introducir, luego pida esos números, y
# muestre un mensaje cada vez que un número no sea mayor que el anterior.

cantidad_numeros = int(input("¿Cuántos números vas a introducir? "))

if cantidad_numeros > 0:
    numero_anterior = int(input("Introduce el primer número: "))
    for i in range(1, cantidad_numeros):
        numero_actual = int(input("Introduce el siguiente número: "))
        if numero_actual <= numero_anterior:
            print("El número introducido no es mayor que el anterior.")
        numero_anterior = numero_actual
else:
    print("No se han introducido números.")


## Ejercicio 10:
# > Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla 
# el número de veces que aparece la letra en la frase.
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

contador = frase.count(letra)
print(f"La letra '{letra}' aparece {contador} veces en la frase.")


## Ejercicio 11:
# > Escriba un programa que pregunte cuantos números se van a introducir, pida los esos números (que puedan ser decimales)
# y calcule su suma, mostrar por terminal la suma de los números introducidos.
cantidad_numeros = int(input("¿Cuántos números vas a introducir? "))

suma = 0
for i in range(cantidad_numeros):
    numero = float(input("Introduce un número: "))
    suma += numero
print("La suma de los números introducidos es:", suma)



# Ejercicio 12:
# > Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos 
# negativos ha introducido.
num_numeros = int(input("¿Cuántos números vas a introducir? "))
contador_negativos = 0

for i in range(num_numeros):
    numero = int(input(f"Introduce el número {i+1}: "))
    if numero < 0:
        contador_negativos += 1
print(f"Has introducido {contador_negativos} números negativos.")