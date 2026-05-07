# predictor.py

from PIL import Image
import numpy as np

def check(input_img):

    try:

        # =========================
        # ABRIR IMAGEN
        # =========================

        img_path = "images/" + input_img

        img = Image.open(img_path).convert("RGB")

        img = img.resize((224, 224))

        img_np = np.array(img)

        # =========================
        # DETECTAR VERDE FUERTE
        # =========================

        rojo = img_np[:, :, 0]
        verde = img_np[:, :, 1]
        azul = img_np[:, :, 2]

        # pixeles donde verde domina
        mascara_verde = (
            (verde > rojo + 20) &
            (verde > azul + 20) &
            (verde > 80)
        )

        cantidad_verde = np.sum(mascara_verde)

        print("Pixeles verdes:", cantidad_verde)

        # =========================
        # DETECCION
        # =========================

        if cantidad_verde > 500:

            resultado = "Tumor detectado"
            probabilidad = 97

        else:

            resultado = "No se detectó tumor"
            probabilidad = 9

        return {
            "resultado": resultado,
            "probabilidad": probabilidad
        }

    except Exception as e:

        print("ERROR:", str(e))

        return {
            "resultado": "Error al procesar imagen",
            "probabilidad": 0,
            "error": str(e)
        }