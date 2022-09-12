from curses.ascii import isupper
import re

#ejercicio 1
"""
texto = input("ingresar texto:")
texto[0]
if texto[0].isupper == True:
    print("la primer letra es mayuscula")
else:
    print("la primer letra es minuscula")
"""
#ejercicio 2
"""
numero = int(input("Ingresa un número: "))
if numero & 1 == 0:
    print("El número es par")
else:
    print("El número es impar")
"""
#ejercicio 3
"""
numero = int(input("ingresar numero:"))
if numero < 1:
    print("debe ser mayor a 1")
if numero > 6:
    print("debe ser menor a 6")
if numero == 1:
    print("6")
if numero == 2:
    print("5")
if numero == 3:
    print("4")
if numero == 4:
    print("3")
if numero == 5:
    print("2")    
if numero == 6:
    print("1")   
"""
#ejercicio 4
"""
zona_de_envio = input("ingresar la zona del envio:")
peso = input("ingresar peso del paquete en gramos:")

if zona_de_envio == 1 and peso <= 5000:
    precio_gramo1 = 10
    precio_envio1 = peso * precio_gramo1
    print(precio_envio1)
if zona_de_envio == 2 and peso <= 5000:
    precio_gramo2 = 15
    precio_envio2 = peso * precio_gramo2
    print(precio_envio2)
if zona_de_envio == 3 and peso <= 5000:
    precio_gramo3 = 18
    precio_envio3 = peso * precio_gramo3
    print(precio_envio3)
if zona_de_envio == 4 and peso <= 5000:
    precio_gramo4 = 24
    precio_envio4 = peso * precio_gramo4
    print(precio_envio4)
if zona_de_envio == 5 and peso <= 5000:
    precio_gramo5 = 30
    precio_envio5 = peso * precio_gramo5
    print(precio_envio5)
"""
#ejercicio 5
"""
fecha = int(input("ingresar numero del dia de la semana:"))
if fecha < 1:
    print("numero incorrecto")
if fecha > 7:
    print("numero incorrecto")

if fecha == 1:
    print("lunes")
if fecha == 2:
    print("martes")
if fecha == 3:
    print("miercoles")
if fecha == 4:
    print("jueves")
if fecha == 5:
    print("viernes")
if fecha == 6:
    print("sabado")
if fecha == 7:
    print("domingo")
"""
#ejercicio 6
"""
caracter_1 = input("caracter 1:")
caracter_2 = input("caracter 2:")
caracter_3 = input("caracter 3:")
caracter_4 = input("caracter 4:")
caracter_5 = input("caracter 5:")

lista1 = [caracter_1, caracter_2, caracter_3, caracter_4, caracter_5]
lista2 = list(reversed(lista1))
print(lista2)
"""
#ejercicio 7
"""
lista = []
numero = int(input("ingresa un numero en la lista:"))
while numero>=0:
	lista.append(numero)
	numero = int(input("ingresa un numero en la lista:"))

if numero <0:
    print(lista)
"""
#ejercicio 8
"""
numero1 = int(input("ingresa un numero en la lista:"))
numero2 = int(input("ingresa un numero en la lista:"))
numero3 = int(input("ingresa un numero en la lista:"))
numero4 = int(input("ingresa un numero en la lista:"))
numero5 = int(input("ingresa un numero en la lista:"))
numero6 = int(input("ingresa un numero en la lista:"))
numero7 = int(input("ingresa un numero en la lista:"))
numero8 = int(input("ingresa un numero en la lista:"))
numero9 = int(input("ingresa un numero en la lista:"))
numero10 = int(input("ingresa un numero en la lista:"))
lista1 = [numero1, numero2, numero3, numero4, numero5]
lista2 = [numero6, numero7, numero8, numero9, numero10]
lista3 = [lista1[0]+lista2[0],lista1[1]+lista2[1],lista1[2]+lista2[2],lista1[3]+lista2[3],lista1[4]+lista2[4]]
print(lista3)
"""
#ejercicio 9 
"""
alumnos = []
edades = []

while True :
    nombre = (input("ingresa el nombre del alumno:"))
    if nombre != "*":
        alumnos.append(nombre)
        edades.append(int(input("ingresa la edad del alumno:")))
    else:
        edad_maxima = max(edades)
        print (edad_maxima)
        for nombre,edad in zip(nombre,edades):
	        if edad == edad_maxima:
                    print(nombre)
"""
#ejercicio10
"""
palabra = "Aguada"
letra_A = palabra.count("A")
letra_g = palabra.count("g")
letra_u = palabra.count("u")
letra_a = palabra.count("a")
letra_d = palabra.count("d")

print(letra_A)
print(letra_g)
print(letra_u)
print(letra_a)
print(letra_d)
"""
#ejercicio11
palabra = "aguada"
letras_faltantes = palabra.count()

