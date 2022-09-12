
#ejercicio1
"""
import re

string = "informatica"

def caracteres_permitidos(string):
    return bool(re.search('[a-zA-Z0-9,]',string))

print(caracteres_permitidos)
"""

#ejercicio2 doble negacion:terminado
"""
import re 
    
string = "universidad"

def caracteres_permitidos(string):
        return not bool(re.search('[^a-zA-Z0-9]', string))
    
print("el string", "ABCDEFabcdef123450", "tiene caracteres permitidos")

"""
#ejercicio3 primer corchete:terminado

""""" 
import re 

def encontrar_patron(string):
    patron = "he*"
    if re.search(patron, string) is not None:
        return "se encontro el patron"
    else:
        return "no se encontro el patron"

print(encontrar_patron("a"))

  #como se ejecuta:   
if re.search("he*", "a") is not None:
    return "se encontro el patron"
else:
    return "no se encontro el patron"
"""

#ejercicio3

"""""
import re

def encontrar_patron(string):
    patron = "he+"
    if re.search(patron, string) is not None:
        return "no se encontro el patron"
    else:
        return "no se encontro el patron"


print(encontrar_patron("a"))
"""

#ejercicio4 
"""
import re 

string = "basura"

def palabras_unidas(string):
    patron = "^[a-z]+_[a-z]+$"
    if re.search(patron,string) is not None:
        return "patron encontrado"
    else:
        return "patron no encontrado"
"""
#ejercicio5
"""
import re
palabra = "dario"
numero = 5
def palabras(palabra):
    patron = "\A5"
    if re.search(patron, palabra) is not None:
        return "comienza con el numero 5"
    else:
        return "no comienza con el numero 5"

print(palabras)
"""
