import random
import string

class JuegoAhorcado:
    def __init__(self, palabra):  
        self.palabra = palabra
        self.vidas = 6
        self.letras_acertadas = []
        self.letras_erroneas = []
        self.ganado = False
        self.terminado = False

    
    def seleccionar_palabra_aleatoria(lista_palabras):
        if not lista_palabras:  # Si la lista está vacía
            raise ValueError("La lista de palabras no puede estar vacía.")
        
        return random.choice(lista_palabras)

    def adivinar_letra(self, letra):
        
        if self.esta_terminado():
            raise RuntimeError("El juego ya terminó.")
        
        if not self.validar_letra(letra):
            raise ValueError("La letra debe ser un caracter alfabético único.")
        
        if letra in self.palabra:
            if letra not in self.letras_acertadas:
                self.letras_acertadas.append(letra)
            if all(l in self.letras_acertadas for l in set(self.palabra)):
                self.ganado = True
            return True
        else:
            if letra not in self.letras_erroneas:
                self.letras_erroneas.append(letra)
                self.quitar_vida()
            return False
        
    def adivinar_palabra(self, intento):
        if self.terminado:
            raise RuntimeError("El juego ya terminó.")
        
        self.validar_palabra(intento)
    
        if intento == self.palabra:
            return True
        else:
            self.quitar_vida()
            return False  
        
    def mostrar_letras_acertadas(self):
        return self.letras_acertadas
    
    def mostrar_letras_erroneas(self):
        return self.letras_erroneas
    
    def esta_ganado(self):
        return self.ganado
   
    def esta_derrotado(self):
        return self.vidas <= 0
    
    def quitar_vida(self):
        if self.vidas > 0:        
            self.vidas -= 1

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
    
    