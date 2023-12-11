import matplotlib.pyplot as plt
import os
import numpy as np
from keras.utils import plot_model
import shutil

# Muestra 15 imágenes y sus etiquetas en una cuadrícula.
# Parameters:
# - x: Imágenes.
# - y: Etiquetas.
# - set_init: Índice de la primera imagen a mostrar.
def show_data(x, y, set_init=0):
    # Crear una figura de 15 subgráficos (3 filas x 5 columnas)
    fig = plt.figure(figsize=(15, 10))

    # Iterar sobre los primeros 15 elementos
    for id in np.arange(15):  # sólo imprimo 15
        # Agregar un subgráfico a la figura
        ax = fig.add_subplot(3, 5, id+1, xticks=[], yticks=[])

        # Mostrar la imagen en el subgráfico en escala de grises
        ax.imshow(x[id + set_init], cmap=plt.cm.binary)

        # Establecer el título del subgráfico con la etiqueta correspondiente
        ax.set_title(str(y[id + set_init]))

    # Guardar la figura en lugar de mostrarla
    plt.savefig("data/sample_images.png")
    plt.close('all')  # Cerrar la figura


# Guarda un gráfico de barras con los resultados de entrenamiento y prueba.
# Parameters:
# - train_loss: Pérdida en entrenamiento.
# - train_accuracy: Precisión en entrenamiento.
# - test_loss: Pérdida en prueba.
# - test_accuracy: Precisión en prueba.
# - model_type: Tipo de modelo ('CNN', 'MLP', 'Simple Model').
# - model_name: Nombre del modelo.
def save_results_to_png(train_loss, train_accuracy, test_loss, test_accuracy, model_type, model_name):

    if not os.path.exists("results"):
        os.makedirs("results")

    # Crear un gráfico de barras con etiquetas
    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(['Train Accuracy', 'Test Accuracy', 'Train Loss', 'Test Loss'],
                  [train_accuracy, test_accuracy, train_loss, test_loss],
                  color=['blue', 'green', 'red', 'orange'])

    # Agregar etiquetas con los porcentajes
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2%}', ha='center', va='bottom')

    ax.set_ylabel('Value')
    ax.set_title(f'Results for {model_name} ({model_type})')
    plt.savefig(f"results/{model_type}_results.png")
    plt.close('all')


# Guarda los resultados en un archivo de texto.
# Parameters:
#     - nombre_modelo: Nombre del modelo.
#     - tiempo_entrenamiento: Tiempo empleado en el entrenamiento.
#     - resultados_train: Resultados en el conjunto de entrenamiento.
#     - resultados_test: Resultados en el conjunto de prueba.
#     - model_type: Tipo de modelo ('cnn', 'mlp', 'simple_model').
def save_results_to_txt(nombre_modelo, tiempo_entrenamiento, resultados_train, resultados_test, model_type):
    
    results_dir = f"results/{model_type.lower()}"
    if os.path.exists(results_dir):
        shutil.rmtree(results_dir)

    os.makedirs(results_dir)

    with open(f"{results_dir}/{nombre_modelo}_resultados.txt", "w") as f:
        # Model
        f.write(f"Modelo: {nombre_modelo}\n")
        f.write(f"- Tiempo empleado: {tiempo_entrenamiento} s\n")
        f.write("- Conjunto:\n")

        # Train
        f.write("  - Train:\n")
        f.write(f"    - Accuracy: {resultados_train['accuracy']}\n")
        f.write(f"    - Loss: {resultados_train['loss']}\n")

        # Test
        f.write("  - Test:\n")
        f.write(f"    - Accuracy: {resultados_test['accuracy']}\n")
        f.write(f"    - Loss: {resultados_test['loss']}\n")


# Guarda la arquitectura del modelo como una imagen.
# Parameters:
# - model: Modelo de Keras.
# - model_type: Tipo de modelo ('cnn', 'mlp', 'simple_model').
# - model_name: Nombre del modelo.
def save_model_architecture_to_image(model, model_type, model_name):

    if not os.path.exists("model_architecture_images"):
        os.makedirs("model_architecture_images")

    # Guardar la arquitectura del modelo como una imagen
    plot_model(model, to_file=f"model_architecture_images/Model_Sequencial_{model_type}_{model_name}.png", show_shapes=True, show_layer_names=True)


# Guarda gráficos de la pérdida y precisión en entrenamiento y validación.
# Parameters:
# - history: Historial de entrenamiento del modelo.
# - model_type: Tipo de modelo ('cnn', 'mlp', 'simple_model').
# - model_name: Nombre del modelo.
def plot_training_history(history, model_type, model_name):

    if not os.path.exists("training_history"):
        os.makedirs("training_history")

    # Plot de la pérdida en entrenamiento y validación
    plt.plot(history.history['loss'], label='Train Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title(f'{model_name} - Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.savefig(f"training_history/{model_type}_{model_name}_loss.png")
    plt.close()

    # Plot de la precisión en entrenamiento y validación
    plt.plot(history.history['accuracy'], label='Train Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title(f'{model_name} - Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.savefig(f"training_history/{model_type}_{model_name}_accuracy.png")
    plt.close()