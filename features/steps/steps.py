from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def _parse_letters(letras_csv):
    cleaned = letras_csv.replace('"', "").replace("'", "")
    parts = [
        part.strip()
        for part in cleaned.replace(",", " ").split()
        if part.strip()
    ]
    return [p.lower() for p in parts]


@given('el servidor Flask está corriendo con la palabra "{palabra}"')
def step_open_browser(context, palabra=None):
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)

    if palabra:
        url = "http://127.0.0.1:5000/set_palabra/" + palabra
        context.driver.get(url)
        time.sleep(0.5)
    else:
        context.driver.get("http://127.0.0.1:5000")
        time.sleep(1)


@when('ingreso las letras "{letras_csv}" en ese orden')
@when('ingreso las letras "{letras_csv}"')
@when(
    'ingreso las letras "{letras_csv}" en el campo de intento '
    "y presiono el botón"
)
def step_try_letters(context, letras_csv):
    letras = _parse_letters(letras_csv)

    for letra in letras:
        input_box = context.driver.find_element(By.NAME, "intento")
        input_box.clear()
        input_box.send_keys(letra)

        button = context.driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )
        button.click()
        time.sleep(0.5)


@when('ingreso "{texto}" en el campo de intento y presiono el botón')
def step_input_text(context, texto):
    input_box = context.driver.find_element(By.NAME, "intento")
    input_box.clear()
    input_box.send_keys(texto)

    button = context.driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    )
    button.click()
    time.sleep(0.5)


@then("el juego debe estar ganado")
def step_then_won(context):
    body = context.driver.page_source
    assert "🎉 ¡Ganaste!" in body, "El juego no muestra mensaje de victoria."


@then("el juego debe estar derrotado")
def step_then_lost(context):
    body = context.driver.page_source
    assert "💀 Perdiste." in body, "El juego no muestra mensaje de derrota."


@then('debo ver el mensaje "{mensaje}" en la página')
def step_check_message(context, mensaje):
    body = context.driver.page_source
    assert mensaje in body, (
        f"No se encontró el mensaje esperado: {mensaje}"
    )


@then("las vidas deben ser {vidas: d}")
def step_then_vidas(context, vidas):
    vidas_text = context.driver.find_element(
        By.XPATH,
        "//p[starts-with(normalize-space(), 'Vidas restantes')]",
    ).text

    corazones = vidas_text.count("❤️")
    assert corazones == vidas, (
        f"Esperaba {vidas} vidas, pero se encontraron "
        f"{corazones} en: {vidas_text}"
    )


@then("la cantidad de letras erróneas debe ser {cant: d}")
def step_then_erroneas(context, cant):
    errores_text = context.driver.find_element(
        By.XPATH,
        "//p[contains(text(), 'Erróneas')]"
    ).text

    letras = errores_text.split(":")[-1].strip()
    num = len(letras.split()) if letras else 0

    assert num == cant, (
        f"Esperaba {cant} letras erróneas, pero hay {num}"
    )


@then("cierro el navegador")
def step_close_browser(context):
    context.driver.quit()
