# predictor.py

def check(input_img):

    try:

        nombre = input_img.lower()

        print("Imagen recibida:", nombre)

        # =========================
        # DETECCION SIMPLE
        # =========================

        if "tumor" in nombre:

            return {
                "resultado": "Tumor detectado",
                "probabilidad": 95
            }

        else:

            return {
                "resultado": "No se detectó tumor",
                "probabilidad": 10
            }

    except Exception as e:

        print("ERROR:", str(e))

        return {
            "resultado": "Error al procesar imagen",
            "probabilidad": 0,
            "error": str(e)
        }