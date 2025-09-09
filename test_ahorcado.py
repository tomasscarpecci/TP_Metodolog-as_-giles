import pytest
from ahorcado import JuegoAhorcado

def test_adivino_letra_en_palabra():
    juego = JuegoAhorcado("python")
    resultado = juego.adivinar_letra("p")
    assert resultado is True
    assert "p" in juego.letras_acertadas

def test_adivino_letra_no_en_palabra():
    juego = JuegoAhorcado("python")
    juego.vidas = 6
    resultado = juego.adivinar_letra("z")
    assert resultado is False
    assert "z" in juego.letras_erroneas