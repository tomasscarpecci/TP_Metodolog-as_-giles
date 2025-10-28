import random
import string
from wordfreq import top_n_list
from recursos.lista_palabras import lista_palabras


class JuegoAhorcado:
    def __init__(self, palabra):
        if palabra:
            self.palabra = palabra.lower()
        else:
            self.palabra = self.seleccionar_palabra_aleatoria(lista_palabras).lower()

        self.vidas = 6
        self.letras_acertadas = []
        self.letras_erroneas = []
        self.ganado = False
        self.terminado = False

    def reiniciar_con_palabra(self, nueva_palabra):
        if " " in nueva_palabra:
            raise ValueError("La palabra no puede contener espacios.")

        self.palabra = nueva_palabra.lower()
        self.vidas = 6
        self.letras_acertadas = []
        self.letras_erroneas = []
        self.ganado = False

    def seleccionar_palabra_wordfreq(idioma="es", cantidad=1000):
        lista_palabras = top_n_list(idioma, cantidad)
        if not lista_palabras:
            raise ValueError("La lista de palabras no puede estar vacía.")
        return random.choice(lista_palabras)

    @staticmethod
    def seleccionar_palabra_aleatoria(lista_palabras):
        if not lista_palabras:
            raise ValueError("La lista de palabras no puede estar vacía.")
        return random.choice(lista_palabras)

    def adivinar_letra(self, letra):

        if self.esta_terminado():
            raise RuntimeError("El juego ya terminó.")

        if not self.validar_letra(letra):
            raise ValueError("La letra debe ser un caracter alfabético único.")
        letra = letra.lower()

        if letra in self.letras_acertadas or letra in self.letras_erroneas:
            raise ValueError("Ya intentaste esa letra.")

        if letra in self.palabra:
            if letra not in self.letras_acertadas:
                self.letras_acertadas.append(letra)
            if all(letra in self.letras_acertadas for letra in set(self.palabra)):
                self.ganado = True
            return True
        else:
            if letra not in self.letras_erroneas:
                self.letras_erroneas.append(letra)
                self.quitar_vida()
            return False

    def adivinar_palabra(self, intento):
        if self.esta_terminado():
            raise RuntimeError("El juego ya terminó.")
        self.validar_palabra(intento)
        if intento.lower() == self.palabra.lower():
            self.ganado = True
            self.terminado = True
            return True
        else:
            self.quitar_vida()
            return False

    def mostrar_letras_acertadas(self):
        return list(self.letras_acertadas)

    def mostrar_letras_erroneas(self):
        return list(self.letras_erroneas)

    def esta_ganado(self):
        return self.ganado

    def esta_derrotado(self):
        return self.vidas <= 0

    def quitar_vida(self):
        self.vidas -= 1
        if self.vidas <= 0:
            self.vidas = 0
            self.terminado = True
            self.ganado = False

    def validar_letra(self, letra):
        return len(letra) == 1 and letra in string.ascii_letters

    def esta_terminado(self):
        return self.esta_derrotado() or self.esta_ganado()

    def validar_palabra(self, palabra):
        if not palabra:
            raise ValueError("La palabra no puede estar vacía.")
        if " " in palabra:
            raise ValueError("La palabra no puede contener espacios.")
        if not all(c in string.ascii_letters for c in palabra):
            raise ValueError("La palabra solo puede contener letras.")
        return True

