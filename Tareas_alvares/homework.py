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


# Ejercicio 13
# Vamos a diseñar una calculadora que se enciende y hasta que no tecleamos SAL no se apaga.
# Esta calculadora funciona de la siguiente manera:
# Recogemos los datos A y B
# Si operación es 1 calcula la raíz cuadrada de la suma de A y B
# Si operación es 2 calcula A / B. Vigilamos que B no sea 0...
# Si la operación es 3 calculamos la siguiente fórmula: ( A * B ) / 2.5
datos="A","B"
while True:
    A=int(input("ingrese el dato A: "))
    B=int(input("ingrese el  dato B: "))
    print("1. raiz cuadrada de la suma de A y B")
    print("2. calcular A/B. el dato b tiene que ser > 0")
    print("3. calcular (A * B)/2.5")
    opcion=input("elija una opcion(1/2/3): ")
    if opcion==1:
        resultado=A + B
        print((resultado))
        break





# Ejercicio 14
# Tenemos la pantalla del móvil bloqueada. Partiendo de un PIN_SECRETO, intentaremos desbloquear la pantalla. Tenemos hasta 3 intentos.
# Simula el proceso con Python. En caso de acceder, lanza al usuario login correcto. Sino, llamando ala policía.
pin_secreto=7133
intentos=3
while intentos >0:
    pin=int(input("ingrese el pin: "))
    if pin==pin_secreto:
        print("login correcto")
        break
    else:
        intentos-=1
        if intentos > 0:
            print(f"pin secreto incorrecto.te queda {intentos} ententos")
        else:
            print("acceso denegado !LLAMANDO A LA POLICIA¡")




# Ejercicio 15
# Crea un algoritmo para la sucesión de Fibonacci. La sucesión de Fibonacci es la siguiente serie:
#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
# Pista: Empezando por 0 y 1, el siguiente número es la suma de los dos números últimos
def fibonacci(limite):
    a, b = 0, 1
    serie_fibonacci = [a, b]

    while b < limite:
        a, b = b, a + b
        serie_fibonacci.append(b)

    return serie_fibonacci

limite = int(input("Ingrese el límite para la sucesión de Fibonacci: "))
resultado = fibonacci(limite)

print("Sucesión de Fibonacci hasta el límite especificado:")
print(resultado)


# Ejercicio 16
# Desarrolla un programa en Python que permita gestionar una lista de tareas pendientes. El programa debe cumplir con los siguientes requisitos:
# Debe permitir agregar nuevas tareas a la lista.
# Debe permitir marcar tareas como completadas, lo que las eliminará de la lista de tareas pendientes.
# Debe mostrar la lista actual de tareas pendientes.
# Debe proporcionar un menú interactivo que permita al usuario seleccionar entre las opciones anteriores y salir del programa.
# El menú debe presentar las siguientes opciones:
# Agregar tarea
# Marcar tarea como completada
# Mostrar tareas
# Salir
tareas=[]
while True:
    print("1.agregar tarea")
    print("2.marcar tarea como completada")
    print("3.mostrar tareas")
    print("4. salir")
    opcion=input("ingrese una opcion(1/2/3/4): ")
    if opcion=="1":
        nueva_tarea=input("ingrese una nueva tarea: ")
        tareas.append(nueva_tarea)
        print("nueva tarea agregada")
    elif opcion=="2":
        if not tareas:
            print("no hay tareas pendientes")
        else:
            print("tareas pendientes a realizar: ")
            for i, tarea in enumerate(tareas):
                print(f"{i+1}.{tarea}")
                tarea_completada=int(input("ingrese el numero de la tarea completada: "))
                if tarea_completada>0 and tarea_completada<=len (tareas):
                    del tareas[tarea_completada-1]
                    print("tarea marcada como completada")
                else:
                    print("numero de tarea invalido")
    elif opcion=="3":
        print("lista de tareas pendintes: ")
        for i, tarea in enumerate(tareas):
            print(f"{i + 1}.{tarea}")
    elif opcion=="4":
        print("!HASTA LUEGO¡")
        break
    else:
        print("opcion invalida !ingrese una opcion valida¡")



# Ejercicio 17
# Crea un programa en Python que simule el funcionamiento de un cajero automático. El programa debe permitir al usuario realizar las siguientes operaciones:
# Verificar el saldo de su cuenta.
# Depositar dinero en su cuenta.
# Retirar dinero de su cuenta.
# Salir del programa.
# El programa debe iniciar con un saldo inicial predeterminado y mostrar un menú con las siguientes opciones:
# Verificar saldo
# Depositar dinero
# Retirar dinero
# Salir
saldo = 1000
while True:
    print("eres bienvenido al cajero automatico de bcp")
    print("1.verificar saldo de su cuenta.")
    print("2.depositar dinero en su cuenta")
    print("3.retirar dinero de su cuenta")
    print("4.salir del programa")
    opcion=input("seleccione una opcion (1/2/3/4):")
    if opcion=="1":
        print(f"el saldo de su cuenta es: ${saldo}")
        break
    elif opcion=="2":
        deposito=float(input("ingrese la cantidad que quiere depositar asu cuenta de bcp:$"))
        saldo+=deposito
        print(f"se ha depositado ${deposito} en su cuenta de bcp.saldo actual ${saldo}   !gracias por su confianza¡")
        break
    elif opcion=="3":
        retiro=float(input("ingrese la cantidad a retirar: $"))
        if retiro>saldo:
            print("dinero insuficiente. ingrese un monto menor.")
        else:
            saldo-=retiro
            print(f"se ha retirado ${retiro} de su cuenta bcp. saldo actual $ {saldo}")
            break
    elif opcion=="4":
        print("gracias por su confianza !HASTA LUEGO¡")
        break
    else:
        print("opcion invalida vuelve a seleccionar la opcion que quieres realizar !gracias¡.")



# Ejercicio 18
# Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan.
codicion=True
while True:
    contraseña=input("ingrese la contraseña: ")
    contraseña_confirmador=input("escriba de nuevo su contraseña: ")
    if contraseña==contraseña_confirmador:
        print("contraseña cofirmada,!Hasta la vista¡")
        break
    else:
        print("las contraseñas no coinciden. intentelo de nuevo")
        continue
        



