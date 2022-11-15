"""
Escribir una clase llamada circulo que contenga un radio, con un metodo que devuelva el area y otro que 
devuelva el perimetro del circulo.
 * Si se instancia la clase con radio <= 0 mostrar una excepcion indicando un error amigable al usuario
   e impidiendo la instanciacion.
 * Si printeamos el objeto creado debe mostrarse una representacion amigable.
 * El objeto debe tener su atributo radio modificable, si se intenta setear un valor <= 0 mostrar un error
   y no permitir la modificacion.
 * Permitir la multiplicacion del cirulo: Circulo * n debe devolver un nuevo objeto con el radio
   multiplicado por n. No permitir la multiplicacion por numeros <= 0.
"""
from math import pi


class Circulo:
    def __init__(self, radio) -> None:
        self.__radio = radio

    def get_radio(self):
        return self.__radio

    def get_area(self):
        return round(pi * self.__radio**2, 2)

    def get_perimetro(self):
        return round(pi*2*self.__radio, 2)

    def set_radio(self, radio):
        if radio <= 0:
            raise ValueError("El radio no puede ser menor o igual que 0")
        else:
            self.__radio = radio

    def __repr__(self) -> str:
        return f"< Radio: {self.__radio} Area: {self.get_area()} Perimetro: {self.get_perimetro()} >"

    def __mul__(self, n):
        if n <= 0:
            raise ValueError("No se puede multiplicar por 0")
        else:
            return Circulo(self.__radio * n)


c1 = Circulo(10)
print(c1.get_radio())
print(c1.get_area())
print(c1.get_perimetro())

c2 = Circulo(10) * 0
print(c2.get_radio())
print(c2.get_area())
print(c2.get_perimetro())


#print(Circulo(10))