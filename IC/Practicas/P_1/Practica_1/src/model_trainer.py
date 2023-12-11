from keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split

# Tamaño del batch y número de épocas
BATCH_SIZE = 256
EPOCHS = 20

# Función para entrenar un modelo de red neuronal simple.
# Entrena un modelo de red neuronal simple y devuelve el historial de entrenamiento.
#     Parameters:
#     - model (Sequential): Modelo de red neuronal a entrenar.
#     - x_train (numpy.ndarray): Conjunto de entrenamiento de características.
#     - y_train (numpy.ndarray): Conjunto de entrenamiento de etiquetas.
#     - x_val (numpy.ndarray): Conjunto de validación de características.
#     - y_val (numpy.ndarray): Conjunto de validación de etiquetas.
#     Returns:
#     - history (History): Historial de entrenamiento del modelo.
def train_simple_neuronal_network(model, x_train, y_train, x_val, y_val):
    # Compilar el modelo
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    # Entrenar el modelo
    history = model.fit(
        x_train, y_train,
        batch_size=BATCH_SIZE,
        epochs=EPOCHS,
        verbose=1,
        validation_data=(x_val, y_val)
    )

    return history

# Función para entrenar un modelo de perceptrón multicapa (MLP) con aumento de datos.
# Entrena un modelo de perceptrón multicapa (MLP) con aumento de datos y devuelve el historial de entrenamiento.
#     Parameters:
#     - model (Sequential): Modelo de perceptrón multicapa a entrenar.
#     - x_train (numpy.ndarray): Conjunto de entrenamiento de características.
#     - y_train (numpy.ndarray): Conjunto de entrenamiento de etiquetas.
#     - x_val (numpy.ndarray): Conjunto de validación de características.
#     - y_val (numpy.ndarray): Conjunto de validación de etiquetas.
#     Returns:
#     - history (History): Historial de entrenamiento del modelo.
def train_mlp_model(model, x_train, y_train, x_val, y_val):
    # Configurar el generador de datos con aumento de datos
    datagen = ImageDataGenerator(
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.1,
        zoom_range=0.1
    )
    datagen.fit(x_train)

    # Entrenar el modelo con el generador de datos
    history = model.fit(datagen.flow(x_train, y_train, batch_size=BATCH_SIZE),
                        steps_per_epoch=len(x_train) / BATCH_SIZE,
                        epochs=EPOCHS,
                        validation_data=(x_val, y_val),
                        verbose=1)

    return history

# Función para entrenar un modelo con aumento de datos.
# Entrena un modelo con aumento de datos y devuelve el historial de entrenamiento.
#     Parameters:
#     - model (Sequential): Modelo de red neuronal a entrenar.
#     - x_train (numpy.ndarray): Conjunto de entrenamiento de características.
#     - y_train (numpy.ndarray): Conjunto de entrenamiento de etiquetas.
#     - x_test (numpy.ndarray): Conjunto de prueba de características.
#     - y_test (numpy.ndarray): Conjunto de prueba de etiquetas.
#     Returns:
#     - history (History): Historial de entrenamiento del modelo.
def train_model(model, x_train, y_train, x_test, y_test):

    # Dividir el conjunto de entrenamiento en entrenamiento y validación
    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.1, random_state=1)

    # Aplicar aumento de datos
    datagen = ImageDataGenerator(
        rotation_range=15,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.1,
        zoom_range=0.1
    )
    datagen.fit(x_train)

    # Entrenar el modelo con el generador de datos
    return model.fit(datagen.flow(x_train, y_train, batch_size=BATCH_SIZE),
                     steps_per_epoch=len(x_train) / BATCH_SIZE,
                     epochs=EPOCHS,
                     validation_data=(x_val, y_val),
                     verbose=1)