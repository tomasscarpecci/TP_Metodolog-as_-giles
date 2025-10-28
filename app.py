from flask import Flask, render_template, request, redirect, session, url_for
from ahorcado import JuegoAhorcado
from recursos.lista_palabras import lista_palabras

app = Flask(__name__)
app.secret_key = "ahorcado_flask_secret"


def iniciar_juego():
    """Crea una nueva partida y establece la imagen inicial."""
    juego = JuegoAhorcado(None) 

    session["palabra"] = juego.palabra
    session["vidas"] = juego.vidas
    session["acertadas"] = juego.letras_acertadas
    session["erroneas"] = juego.letras_erroneas

    session["imagen"] = f"img/ahorcado{6 - juego.vidas}.png"

    return juego


def cargar_juego():
    """Reconstruye el juego desde la sesión."""
    palabra = session.get("palabra")
    if not palabra:
        return iniciar_juego()

    juego = JuegoAhorcado(palabra)
    juego.vidas = session.get("vidas", 6)
    juego.letras_acertadas = session.get("acertadas", [])
    juego.letras_erroneas = session.get("erroneas", [])

    session["imagen"] = f"img/ahorcado{6 - juego.vidas}.png"
    return juego

@app.route("/", methods=["GET", "POST"])
def index():
    if "palabra" not in session:
        iniciar_juego()

    juego = cargar_juego()
    mensaje = None
    error = None

    if request.method == "POST":
        intento = request.form.get("intento", "").lower()

        try:
            if len(intento) == 1:
                juego.adivinar_letra(intento)
            else:
                juego.adivinar_palabra(intento)
        except Exception as e:
            error = str(e)
        else:
            session["vidas"] = juego.vidas
            session["acertadas"] = juego.letras_acertadas
            session["erroneas"] = juego.letras_erroneas
            session["imagen"] = f"img/ahorcado{6 - juego.vidas}.png"

            if juego.esta_ganado():
                mensaje = f"🎉 ¡Ganaste! La palabra era '{juego.palabra.upper()}'."
                session.clear()
            elif juego.esta_derrotado():
                mensaje = f"💀 Perdiste. La palabra era '{juego.palabra.upper()}'."
                session.clear()

    return render_template(
        "index.html",
        juego=juego,
        palabra_formateada=formatear_palabra(juego),
        mensaje=mensaje,
        error=error
    )


@app.route("/reiniciar")
def reiniciar():
    """Reinicia completamente la partida."""
    session.clear()
    iniciar_juego()
    return redirect(url_for("index"))

def formatear_palabra(juego):
    """Muestra la palabra con guiones bajos y letras acertadas."""
    return " ".join([l if l in juego.letras_acertadas else "_" for l in juego.palabra])

if __name__ == "__main__":
    app.run(debug=True)
