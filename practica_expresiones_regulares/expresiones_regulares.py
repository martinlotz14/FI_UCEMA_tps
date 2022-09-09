#ejercicio1

import re

def caracteres_permitidos(string):
    return bool(re.search('[a-zA-Z0-9,]',string))

print(caracteres_permitidos)
""""""

#ejercicio2 doble negacion:terminado
"""""
import re 
    
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

#ejercicio4 (foto)


