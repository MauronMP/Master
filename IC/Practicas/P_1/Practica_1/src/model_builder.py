import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import BatchNormalization
from keras.optimizers import Adam

N_CLASSES = 10	# número de clases

# Función para construir y compilar un modelo de red neuronal simple.
# Construye y compila un modelo de red neuronal simple con capas densas.
#     Parameters:
#     - input_shape (tuple): Dimensiones de entrada de las imágenes.
#     - num_classes (int): Número de clases del problema.
#     Returns:
#     - model (Sequential): Modelo de red neuronal construido.
def build_simple_neuronal_network_model(input_shape, num_classes):

    # Crear un modelo secuencial
    model = Sequential([
        Flatten(input_shape=input_shape),
        Dense(128, activation='relu'),
        Dense(64, activation='relu'),
        Dense(num_classes, activation='softmax')
    ])

    # Compilar el modelo con la función de pérdida, el optimizador y las métricas
    model.compile(
        loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
    )

    return model


# Función para construir y compilar un modelo de red neuronal convolucional (CNN).
# Construye y compila un modelo de red neuronal convolucional (CNN).
#     Parameters:
#     - input_shape (tuple): Dimensiones de entrada de las imágenes.
#     Returns:
#     - model (Sequential): Modelo de red neuronal convolucional construido.
def cnn_model(input_shape):
    # Crear un modelo secuencial
    model = Sequential()

    # Agregar capas convolucionales y de pooling
    model.add(Conv2D(64, kernel_size=(5, 5),
                     activation='relu',
                     input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Agregar capa de dropout para regularización
    model.add(Dropout(0.3))

    # Aplanar la salida y agregar capas densas
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dense(128, activation='relu'))

    # Agregar capas de dropout adicionales
    model.add(Dropout(0.2))
    model.add(Dense(50, activation='relu'))
    model.add(Dropout(0.4))

    # Capa de salida con activación softmax para clasificación
    model.add(Dense(N_CLASSES, activation='softmax'))

    # Compilar el modelo con la función de pérdida, el optimizador y las métricas
    model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.Adam(lr=0.001),
                  metrics=['accuracy'])

    return model


# Función para construir y compilar un modelo de red neuronal tipo perceptrón multicapa (MLP).
# Construye y compila un modelo de red neuronal tipo perceptrón multicapa (MLP).
#     Parameters:
#     - input_shape (tuple): Dimensiones de entrada de las imágenes.
#     - num_classes (int): Número de clases del problema.
#     Returns:
#     - model (Sequential): Modelo de perceptrón multicapa construido.
def build_mlp_model(input_shape, num_classes):
    # Crear un modelo secuencial
    model = Sequential([
        Flatten(input_shape=input_shape),
        Dense(512, activation='relu'),
        BatchNormalization(),
        Dropout(0.5),
        Dense(256, activation='relu'),
        BatchNormalization(),
        Dropout(0.5),
        Dense(128, activation='relu'),
        BatchNormalization(),
        Dropout(0.5),
        Dense(64, activation='relu'),
        BatchNormalization(),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])

    # Compilar el modelo con la función de pérdida, el optimizador y las métricas
    model.compile(
        loss='categorical_crossentropy',
        optimizer=Adam(learning_rate=0.0001),
        metrics=['accuracy']
    )

    return model