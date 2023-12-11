from keras.datasets import mnist
from sklearn.model_selection import train_test_split

# Lectura de datos
def read_data():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    # Divide el conjunto de entrenamiento en train y val
    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.1, random_state=1)

    return (x_train, y_train), (x_test, y_test), (x_val, y_val)

# Preprocesa los datos de entrada
# - x_train: entrada del conjunto de entrenamiento.
# - y_train: etiquetas del conjunto de entrenamiento.
# - x_test: entrada del conjunto de test.
# - y_test: etiquetas del conjunto de test.
def summarize_dataset(x_train, y_train, x_test, y_test):
	print('Dimensión de x_train:', x_train.shape, 'y_train:', y_train.shape)
	print('Dimensión de x_test:', x_test.shape, 'y_test:', y_test.shape)
	print(x_train.shape[0], 'ejemplos de entrenamiento')
	print(x_test.shape[0], 'ejemplos de test\n')
	
# Preprocesa los datos de entrada
# - x_train: entrada del conjunto de entrenamiento.
# - x_test: entrada del conjunto de test.
def preprocess_data(x_train, x_test):
	x_train = x_train.astype('float32')	# conversión a float32
	x_test = x_test.astype('float32')	# conversión a float32
	x_train /= 255						# normalización a [0,1]
	x_test /= 255						# normalización a [0,1]