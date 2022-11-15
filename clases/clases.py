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

c2 = Circulo(10) * 2
print(c2.get_radio())
print(c2.get_area())
print(c2.get_perimetro())


#print(Circulo(10))