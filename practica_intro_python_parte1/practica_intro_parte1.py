#ejercicio 1
"""
nombre = input("ingresar nombre:")
print(len(nombre))
"""
#ejercicio 2
"""
apellido = input("apellido:")
longitud_apellido = len(apellido)
if longitud_apellido >= 6:
    print(apellido.upper())
    print(apellido[4:6])
else:
    print("debe contener 6 o mas caracteres")
"""

#ejercicio 3
"""
nombre = input("nombre:")
apellido = input("apellido:")
print ("hola" + nombre + apellido)
"""

#ejercicio 4
"""
nombre = input("nombre:")
apellido = input("apellido:")
segundo_apellido = input("segundo apellido:")
print (nombre[0].upper() + apellido[0].upper() + segundo_apellido[0].upper())
"""
#ejercicio 5
"""
numero_1 = int(input ("ingresar numero 1:"))
numero_2 = int(input ("ingresar numero 2:"))
numero_3 = int(input ("ingresar numero 3:"))

numero=(numero_1 + numero_2 + numero_3)
resultado=(numero/3)
print(resultado)
"""
#ejercicio 6
"""
minutos = int(input("ingresar minutos:"))
horas = minutos/60
minutos_de_hora = minutos - 60 * horas
print("son")
print(horas)
print("horas y")
print()
print("minutos")
"""
#ejercicio 7
"""
sueldo_base = 100
cantidad_de_ventas = int(input("cantidad de ventas:"))
venta = int(input("valor de venta:"))
comision = venta * 0.10

if cantidad_de_ventas >= 4:
    sueldo = sueldo_base + comision * cantidad_de_ventas
    print(sueldo)
else:
    print(sueldo_base)
"""
#ejercicio 8 
"""
respuestas_correctas = int(input("cantidad respuestas correctas:"))
respuestas_incorrectas = int(input("cantidad  respuestas incorrectas:"))

puntaje_correctas = respuestas_correctas * 4
print(puntaje_correctas)
puntaje_incorrectas = respuestas_incorrectas * -1
print(puntaje_incorrectas)

puntaje_final = puntaje_correctas + puntaje_incorrectas
print(puntaje_final)
"""