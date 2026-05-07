# predictor.py

import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.optimizers import RMSprop

# =========================
# CARGAR MODELO
# =========================

saved_model = load_model("model/VGG_model.h5")

# =========================
# RECOMPILAR MODELO
# =========================

optimizer = RMSprop(
    learning_rate=0.001
)

saved_model.compile(
    optimizer=optimizer,
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# =========================
# PREDICCION
# =========================

def check(input_img):

    try:

        print("Imagen recibida:", input_img)

        # =========================
        # RUTA IMAGEN
        # =========================

        img_path = "images/" + input_img

        print("Ruta imagen:", img_path)

        # =========================
        # CARGAR IMAGEN
        # =========================

        img = Image.open(img_path).convert("RGB")

        img = img.resize((224, 224))

        # =========================
        # PREPROCESAMIENTO
        # =========================

        img = np.array(img)

        img = img / 255.0

        img = np.expand_dims(img, axis=0)

        print("Shape:", img.shape)

        # =========================
        # PREDICCION
        # =========================

        output = saved_model.predict(img)

        print("Output modelo:", output)

        prob = float(np.max(output))

        # =========================
        # RESULTADO
        # =========================

        if prob >= 0.5:

            resultado = "Tumor detectado"

        else:

            resultado = "No se detectó tumor"

        print("Resultado:", resultado)
        print("Probabilidad:", prob)

        return {
            "resultado": resultado,
            "probabilidad": round(prob * 100, 2)
        }

    except Exception as e:

        print("ERROR:", str(e))

        return {
            "resultado": "Error al procesar imagen",
            "probabilidad": 0,
            "error": str(e)
        }