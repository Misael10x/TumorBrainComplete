# app.py

import os
from flask import Flask, request
from predictor import check

# =========================
# FLASK
# =========================

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# =========================
# HOME
# =========================

@app.route('/')
def home():

    return {
        "mensaje": "Brain Tumor API funcionando"
    }

# =========================
# UPLOAD Y PREDICCION
# =========================

@app.route('/upload', methods=['POST'])
def upload():

    try:

        # =========================
        # CARPETA IMAGENES
        # =========================

        target = os.path.join(APP_ROOT, 'images')

        if not os.path.isdir(target):

            os.mkdir(target)

        # =========================
        # RECIBIR ARCHIVO
        # =========================

        if 'file' not in request.files:

            return {
                "error": "No se recibió imagen"
            }, 400

        file = request.files['file']

        if file.filename == '':

            return {
                "error": "Archivo inválido"
            }, 400

        # =========================
        # GUARDAR IMAGEN
        # =========================

        filename = file.filename

        filepath = os.path.join(target, filename)

        file.save(filepath)

        print("Imagen guardada:", filepath)

        # =========================
        # PREDICCION
        # =========================

        resultado = check(filename)

        return resultado

    except Exception as e:

        print("ERROR APP:", str(e))

        return {
            "error": str(e)
        }, 500

# =========================
# RUN
# =========================

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )