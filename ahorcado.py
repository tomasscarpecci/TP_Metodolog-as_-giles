import random

class JuegoAhorcado:
    def __init__(self, palabra):
        self.palabra = palabra
        self.vidas = 6
        self.letras_acertadas = []
        self.letras_erroneas = []

    def adivinar_letra(self, letra):
        if letra in self.palabra:
            self.letras_acertadas.append(letra)
            return True
        else:
            self.letras_erroneas.append(letra)
            self.vidas -= 1
            return False
        
    def adivinar_palabra(self, intento):
        if intento == self.palabra:
            return True
        else:
            self.vidas -= 1
            return False  
        
    def mostrar_letras_acertadas(self):
        return self.letras_acertadas