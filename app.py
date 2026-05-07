import os
from flask import Flask, render_template, request, send_from_directory
from predictor import check

author = 'TEAM DELTA'

# =========================
# FLASK
# =========================

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# =========================
# MOSTRAR IMAGENES
# =========================

@app.route('/images/<filename>')
def images(filename):

    return send_from_directory(
        os.path.join(APP_ROOT, 'images'),
        filename
    )

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

        # =========================
        # CARPETA IMAGENES
        # =========================

        target = os.path.join(APP_ROOT, 'images/')

        print(target)

        if not os.path.isdir(target):

            os.mkdir(target)

        # =========================
        # RECIBIR ARCHIVO
        # =========================

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

        # =========================
        # GUARDAR IMAGEN
        # =========================

        filename = file.filename

        dest = os.path.join(target, filename)

        print(f"Saving file to: {dest}")

        file.save(dest)

        # =========================
        # PREDICCION
        # =========================

        resultado = check(filename)

        # =========================
        # MOSTRAR RESULTADO
        # =========================

        return {
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