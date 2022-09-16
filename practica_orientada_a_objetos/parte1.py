#ejercicio 3

"""
class Notebook:
  def __init__(self, marca, modelo, precio):
    self.marca = marca
    self.modelo = modelo
    self.precio = precio 

  def descuento(self,porcentaje):
    self.precio = self.precio - self.precio * porcentaje/100

  def precioActual(self):
    return self.precio


notebook1 = Notebook("asus", "R556L", 80000)
notebook1.descuento(50)
print(notebook1.precioActual())
"""

#ejercicio 4

"""
class Contador:
  def __init__(self, valor):
    self.valor = valor 

  def inc(self):
    self.valor += 1

  def dis(self):
    self.valor -= 1

  def reset(self):
    self.valor = 0

  def valorActual(self):
    print(self.valor)

  def valorNuevo(self, nuevoValor):
    self.valor = nuevoValor
"""

#ejercicio5
"""
class Contador:
  def __init__(self, valor):
    self.valor = valor 
    self.comando = None

  def inc(self):
    self.valor += 1
    self.comando = "incremento"

  def dis(self):
    self.valor -= 1
    self.comando = "disminucion"


  def reset(self):
    self.valor = 0
    self.comando = "reseteo"

  def valorActual(self):
    print(self.valor)
    self.comando = "valor actual"

  def valorNuevo(self, nuevoValor):
    self.valor = nuevoValor
    self.comando = "valor nuevo"

  def ultimoComando(self):
    print(self.comando)

"""

#ejercicio 6(foto)