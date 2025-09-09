import pytest
from ahorcado import JuegoAhorcado

def test_adivino_letra_que_esta_en_palabra():
    juego = JuegoAhorcado("python")
    resultado = juego.adivinar_letra("p")
    assert resultado is True
    assert "p" in juego.letras_acertadas