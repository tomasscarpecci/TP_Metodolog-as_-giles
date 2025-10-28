from behave import given, when, then
from ahorcado import JuegoAhorcado

def _parse_letters(letras_csv):
    s = letras_csv.replace('"', '').replace("'", "")
    parts = [p.strip() for p in s.replace(',', ' ').split() if p.strip()]
    return [p.lower() for p in parts]

@given('un juego iniciado con la palabra "{palabra}"')
def step_init_game(context, palabra):
    context.juego = JuegoAhorcado(palabra.lower())

@given('un juego iniciado al azar')
def step_init_random(context):
    context.juego = JuegoAhorcado()

@when('intento las letras "{letras_csv}" en ese orden')
@when('intento las letras "{letras_csv}"')
@when('intento las letras incorrectas "{letras_csv}"')
def step_try_letters(context, letras_csv):
    letras = _parse_letters(letras_csv)
    for letra in letras:
        if context.juego.esta_terminado():
            break
        context.juego.adivinar_letra(letra)

@then('el juego debe estar ganado')
def step_then_won(context):
    assert context.juego.esta_ganado(), (
        f"Esperaba que el juego estuviera ganado, pero no lo está. "
        f"Palabra: {context.juego.palabra}, "
        f"Acertadas: {context.juego.letras_acertadas}, "
        f"Errores: {context.juego.letras_erroneas}, "
        f"Vidas: {context.juego.vidas}"
    )

@then('el juego debe estar derrotado')
def step_then_lost(context):
    assert context.juego.esta_derrotado(), (
        f"Esperaba que el juego estuviera perdido, pero no lo está. "
        f"Palabra: {context.juego.palabra}, "
        f"Vidas: {context.juego.vidas}"
    )

@then('las vidas deben ser {vidas:d}')
def step_then_vidas(context, vidas):
    assert context.juego.vidas == vidas, f"Esperaba {vidas} vidas, pero hay {context.juego.vidas}"

@then('la cantidad de letras erróneas debe ser {cant:d}')
def step_then_erroneas(context, cant):
    assert len(context.juego.letras_erroneas) == cant, f"Esperaba {cant} errores, pero hay {len(context.juego.letras_erroneas)}"

@then('la cantidad de letras erróneas debe ser mayor que 0')
def step_then_erroneas_mayor_cero(context):
    assert len(context.juego.letras_erroneas) > 0, "Esperaba al menos 1 letra errónea"
