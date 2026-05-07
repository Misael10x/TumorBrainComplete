# app.py

import os
from flask import Flask, render_template, request
from predictor import check

author = 'TEAM DELTA'

app = Flask(__name__, static_folder="images")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# =========================
# HOME
# =========================

@app.route('/')
@app.route('/index')
def index():
    return render_template('upload.html')

# =========================
# UPLOAD Y PREDICCION
# =========================

@app.route('/upload', methods=['GET', 'POST'])
def upload():

    try:

        target = os.path.join(APP_ROOT, 'images/')

        print(target)

        if not os.path.isdir(target):
            os.mkdir(target)

        files = request.files.getlist('file')

        if not files or files == [None]:

            return {
                "error": "No se recibió ninguna imagen"
            }, 400

        file = files[0]

        if file.filename == '':

            return {
                "error": "Archivo inválido"
            }, 400

        filename = file.filename

        dest = os.path.join(target, filename)

        print(f"Saving file to: {dest}")

        file.save(dest)

        # =========================
        # PREDICCION
        # =========================

        resultado = check(filename)

        return {
            "filename": filename,
            "resultado": resultado["resultado"],
            "probabilidad": resultado["probabilidad"]
        }

    except Exception as e:

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
        port=port,
        debug=True
    )