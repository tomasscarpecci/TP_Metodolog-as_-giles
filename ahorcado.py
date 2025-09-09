import random

class JuegoAhorcado:
    def __init__(self, palabra):
        self.palabra = palabra
        self.letras_acertadas = []
        self.letras_erroneas = []

    def adivinar_letra(self, letra):
        if letra in self.palabra:
            self.letras_acertadas.append(letra)
            return True
        else:
            self.letras_erroneas.append(letra)
            return False
        
    def adivinar_palabra(self, intento):
        return intento == self.palabra
        