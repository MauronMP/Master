from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from time import time
from model_builder import *
from model_trainer import *
from visualization import *

# Función para construir y entrenar modelos de acuerdo al tipo especificado.
# Parameters:
# - model_type (str): Tipo de modelo a construir y entrenar ('cnn', 'mlp', 'simple_model').
# - input_shape (tuple): Dimensiones de entrada de las imágenes.
# - x_train, y_train, x_val, y_val, x_test, y_test: Conjuntos de datos de entrenamiento, validación y prueba.
# - model_name (str): Nombre del modelo para guardar resultados.  
def build_and_train_model(model_type, input_shape, x_train, y_train, x_val, y_val, x_test, y_test, model_name):
    
    # Construir el modelo
    model = None
    if model_type == 'cnn':
        model = cnn_model(input_shape)
    elif model_type == 'mlp':
        model = build_mlp_model(input_shape, N_CLASSES)
    elif model_type == 'simple_model':
        model = build_simple_neuronal_network_model(input_shape, N_CLASSES)


    # Guardar la arquitectura del modelo en una imagen
    save_model_architecture_to_image(model, f'{model_type}_model', f'{model_type.capitalize()}_model')

    # Entrenar el modelo
    start_time = time()

    if model_type == 'cnn':
        history = train_cnn_model(model, x_train, y_train, x_val, y_val)
    elif model_type == 'mlp':
        history = train_mlp_model(model, x_train, y_train, x_val, y_val)
    elif model_type == 'simple_model':
        history = train_simple_neuronal_network(model, x_train, y_train, x_val, y_val)

    plot_training_history(history, model_type, f'{model_type.capitalize()}_model')
    elapsed_time = time() - start_time

    # Evaluar el modelo
    score_train, score_test = model.evaluate(x_train, y_train, verbose=0), model.evaluate(x_test, y_test, verbose=0)

    # Guardar resultados en archivos de texto
    save_results_to_txt(model_type.capitalize(), elapsed_time,
                        {'accuracy': f'{score_train[1]:.6%}', 'loss': f'{score_train[0]:.6%}'},
                        {'accuracy': f'{score_test[1]:.6%}', 'loss': f'{score_test[0]:.6%}'},
                        f'{model_type.lower()}')

    show_data(x_test, y_test)

    # Guardar los 10,000 dígitos etiquetados del conjunto de prueba
    predictions = model.predict(x_test)
    predicted_labels = np.argmax(predictions, axis=1)
    with open('digitos_etiquetas_conjunto_prueba.txt', 'w', encoding='utf-8') as f:
        for label in predicted_labels:
            f.write(str(label))

    # Guardar resultados en imágenes
    save_results_to_png(score_train[0], score_train[1], score_test[0], score_test[1], model_type.lower(), model_type.capitalize())