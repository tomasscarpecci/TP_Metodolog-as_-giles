import pytest
from ahorcado import JuegoAhorcado

def test_inicio_juego_correctamente():
    juego = JuegoAhorcado("python")
    assert juego.palabra == "python"
    assert juego.vidas == 6
    assert juego.letras_acertadas == []
    assert juego.letras_erroneas == []

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
    assert juego.vidas == 5

def test_adivino_palabra_y_acierto():
    juego = JuegoAhorcado("python")
    resultado = juego.adivinar_palabra("python")
    assert resultado is True

def test_adivino_palabra_y_no_acierto():
    juego = JuegoAhorcado("python")
    resultado = juego.adivinar_palabra("java")
    assert resultado is False
    assert juego.vidas == 5
    
def test_mostrar_letras_acertadas():
    juego = JuegoAhorcado("python")
    juego.adivinar_letra("p")
    juego.adivinar_letra("o")
    resultado = juego.mostrar_letras_acertadas()
    assert resultado == ["p", "o"]

def test_mostrar_letras_erroneas():
    juego = JuegoAhorcado("python")
    juego.adivinar_letra("z")
    juego.adivinar_letra("q")
    resultado = juego.mostrar_letras_erroneas()
    assert resultado == ["z", "q"]