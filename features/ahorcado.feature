Feature: Juego del Ahorcado - escenarios ATDD mínimos

  Scenario: El Juego Perfecto
    Given un juego iniciado con la palabra "sol"
    When intento las letras "s", "o", "l" en ese orden
    Then el juego debe estar ganado
    And las vidas deben ser 6

  Scenario: El peor Juego
    Given un juego iniciado con la palabra "python"
    When intento las letras incorrectas "a", "b", "c", "d", "e", "f"
    Then el juego debe estar derrotado
    And las vidas deben ser 0

  Scenario: Gano con algunos errores
    Given un juego iniciado con la palabra "gato"
    When intento las letras "g", "x", "a", "y", "t", "o"
    Then el juego debe estar ganado
    And la cantidad de letras erróneas debe ser 2

  Scenario: Pierdo con algunos errores
    Given un juego iniciado con la palabra "perro"
    When intento las letras "p", "e", "z", "q", "w", "r", "t", "f", "g"
    Then el juego debe estar derrotado
    And la cantidad de letras erróneas debe ser mayor que 0