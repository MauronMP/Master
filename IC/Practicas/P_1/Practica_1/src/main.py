import keras
from keras import backend as K
from data_loader import read_data, summarize_dataset, preprocess_data
from model_builder import *
from model_trainer import *
from build_and_train_model import *
from visualization import *

N_CLASSES = 10				# número de clases
IMG_ROWS, IMG_COLS = 28, 28	# Dimensiones de las imágenes

# Función principal para entrenar y evaluar modelos en el conjunto de datos MNIST.
def main():

    # Lectura de datos de entrenamiento y test
    (x_train, y_train), (x_test, y_test), (x_val, y_val) = read_data()
    summarize_dataset(x_train, y_train, x_test, y_test)
    x_test_orig = x_test.copy()
    show_data(x_test_orig, y_test)

    # Preprocesamiento
    input_shape = (1, IMG_ROWS, IMG_COLS) if K.image_data_format() == 'channels_first' else (IMG_ROWS, IMG_COLS, 1)
    x_train = x_train.reshape(x_train.shape[0], *input_shape)
    x_test = x_test.reshape(x_test.shape[0], *input_shape)
    x_val = x_val.reshape(x_val.shape[0], *input_shape)
    preprocess_data(x_train, x_test)

    # Convirtiendo el vector de etiquetas a una matriz binaria
    y_train_categorical = keras.utils.to_categorical(y_train, N_CLASSES)
    y_test_categorical = keras.utils.to_categorical(y_test, N_CLASSES)
    y_val_categorical = keras.utils.to_categorical(y_val, N_CLASSES)

    # Entrenar y evaluar modelos
    build_and_train_model('cnn', input_shape, x_train, y_train_categorical, x_val, y_val_categorical, x_test, y_test_categorical, 'CNN_model')
    build_and_train_model('mlp', input_shape, x_train, y_train_categorical, x_val, y_val_categorical, x_test, y_test_categorical, 'MLP_model')
    build_and_train_model('simple_model', input_shape, x_train, y_train_categorical, x_val, y_val_categorical, x_test, y_test_categorical, 'simple_model')

if __name__ == "__main__":
    main()