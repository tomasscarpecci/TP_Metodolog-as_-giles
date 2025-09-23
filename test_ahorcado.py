import pytest
from ahorcado import JuegoAhorcado

def test_inicio_juego_correctamente():
    juego = JuegoAhorcado("python")
    assert juego.palabra == "python"
    assert juego.vidas == 6
    assert juego.letras_acertadas == []
    assert juego.letras_erroneas == []
    assert juego.esta_ganado() is False
    assert juego.esta_derrotado() is False
    assert juego.esta_terminado() is False

# Adivinar letras y palabras

def test_no_acepta_palabra_con_espacios():
    juego = JuegoAhorcado("Python")
    with pytest.raises(ValueError):
        juego.adivinar_palabra("Py thon")
    

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

def test_adivino_palabra_y_acierto():
    juego = JuegoAhorcado("python")
    resultado = juego.adivinar_palabra("python")
    assert resultado is True

def test_adivino_palabra_y_no_acierto():
    juego = JuegoAhorcado("python")
    resultado = juego.adivinar_palabra("java")
    assert resultado is False
    
# Mostrar letras acertadas y erroneas

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

#Vida y derrota

def test_no_se_puede_jugar_si_esta_ganado():
    juego = JuegoAhorcado("sol")
    juego.ganado = True
    with pytest.raises(RuntimeError):
        juego.adivinar_letra("a")

def test_no_se_puede_jugar_si_esta_derrotado():
    juego = JuegoAhorcado("python")
    juego.vidas = 0
    with pytest.raises(RuntimeError):
        juego.adivinar_letra("p")
    assert juego.esta_terminado() is True

def test_derrota_al_llegar_a_cero_vidas():
    juego = JuegoAhorcado("python")
    for letra in ["a", "b", "c", "d", "e", "f"]:  
        juego.adivinar_letra(letra)
    assert juego.vidas == 0
    assert juego.esta_derrotado() is True

def test_quitar_vida_metodo():
    juego = JuegoAhorcado("python")
    juego.quitar_vida()
    assert juego.vidas == 5

def test_reducir_vida_por_letra_incorrecta():
    juego = JuegoAhorcado("python")
    juego.adivinar_letra("z")
    assert juego.vidas == 5

def test_reducir_vida_por_palabra_incorrecta():
    juego = JuegoAhorcado("python")
    juego.adivinar_palabra("java")
    assert juego.vidas == 5

#Validacion de letras

def test_valido_letra_alfabetica():
    juego = JuegoAhorcado("python")
    assert juego.validar_letra("a") is True
    assert juego.validar_letra("Z") is True

def test_no_valido_letra_no_alfabetica():
    juego = JuegoAhorcado("python")
    assert juego.validar_letra("1") is False
    assert juego.validar_letra("@") is False
    assert juego.validar_letra("ab") is False
    assert juego.validar_letra("") is False