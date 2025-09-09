import random

class JuegoAhorcado:
    def __init__(self, palabra):
        self.palabra = palabra
        self.letras_acertadas = []

    def adivinar_letra(self, letra):
        if letra in self.palabra:
            self.letras_acertadas.append(letra)
            return True
        return False