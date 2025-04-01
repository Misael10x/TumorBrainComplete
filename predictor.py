import numpy as np
from keras.preprocessing import image
from tensorflow.keras.models import load_model
from tensorflow.keras.optimizers import RMSprop

# Cargar el modelo sin compilarlo para poder modificarlo
saved_model = load_model("model/VGG_model.h5", compile=False)

# Modificar el optimizador (en este caso se utiliza RMSprop)
optimizer = RMSprop(learning_rate=0.001)  # Ajusta el learning_rate si es necesario

# Volver a compilar el modelo con el optimizador y la configuración que desees
saved_model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])

status = True

def check(input_img):
    print("Your image is: " + input_img)

    # Cargar la imagen y redimensionarla
    img = image.load_img("images/" + input_img, target_size=(224, 224))
    img = np.asarray(img)

    # Expandir dimensiones de la imagen para que sea compatible con el modelo
    img = np.expand_dims(img, axis=0)

    # Realizar la predicción con el modelo
    output = saved_model.predict(img)

    # Verificar si la salida corresponde a la clase 1
    if output[0][0] == 1:
        status = True
    else:
        status = False

    print(status)
    return status
