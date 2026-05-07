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
        # ANALISIS SIMPLE
        # =========================

        promedio_verde = np.mean(img_np[:, :, 1])

        promedio_rojo = np.mean(img_np[:, :, 0])

        promedio_azul = np.mean(img_np[:, :, 2])

        brillo_total = (
            promedio_rojo +
            promedio_verde +
            promedio_azul
        ) / 3

        print("Verde:", promedio_verde)
        print("Brillo:", brillo_total)

        # =========================
        # DETECCION SIMPLE
        # =========================

        if promedio_verde > 60:

            resultado = "Tumor detectado"
            probabilidad = 94

        else:

            resultado = "No se detectó tumor"
            probabilidad = 12

        # =========================
        # RESPUESTA
        # =========================

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