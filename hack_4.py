from abc import ABC, abstractmethod
import math


class Figura(ABC):
    @abstractmethod
    def area(self) -> float:
        ...

    @abstractmethod
    def nombre(self) -> str:
        ...

    def info(self) -> str:
        return f"{self.nombre()}: área = {self.area():.2f}"


class Circulo(Figura):
    def __init__(self, radio: float):
        self.radio = radio

    def area(self) -> float:
        return math.pi * self.radio ** 2

    def nombre(self) -> str:
        return "Círculo"


class Rectangulo(Figura):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura

    def nombre(self) -> str:
        return "Rectángulo"


# ── Demo / prueba ──────────────────────────────────────────────
if __name__ == "__main__":
    figuras = [
        Circulo(5),
        Rectangulo(4, 7),
        Circulo(2.5),
        Rectangulo(10, 3),
    ]

    for figura in figuras:
        print(figura.info())