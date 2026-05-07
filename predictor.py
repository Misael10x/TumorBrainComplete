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
        # COLORES
        # =========================

        rojo = np.mean(img_np[:, :, 0])

        verde = np.mean(img_np[:, :, 1])

        azul = np.mean(img_np[:, :, 2])

        print("Rojo:", rojo)
        print("Verde:", verde)
        print("Azul:", azul)

        # =========================
        # DIFERENCIA VERDE
        # =========================

        diferencia_verde = verde - ((rojo + azul) / 2)

        print("Diferencia verde:", diferencia_verde)

        # =========================
        # DETECCION
        # =========================

        if diferencia_verde > 8:

            resultado = "Tumor detectado"
            probabilidad = 96

        else:

            resultado = "No se detectó tumor"
            probabilidad = 8

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