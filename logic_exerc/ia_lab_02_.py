import tensorflow as tf

import matplotlib.pyplot as plt

# Dataset mnist - 60 mil figuras 28x28px
mnist = tf.keras.datasets.mnist
# Carregar os dados de treino e teste
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# Normalização dos dados (figuras) - (0-255) -> (0-1)
x_train, x_test = x_train / 255.0, x_test / 255.0

# Criar uma rede neural
model = tf.keras.models.Sequential([
  # Entrada tem que ser transformada de figuras 28x28 em um vetor
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  # Camada oculta N neurônios utilizando a função de ativação RuLu
  tf.keras.layers.Dense(32, activation='relu'),
  # Camada oculta em X% dos neurônios ativados aleatoriamente
  tf.keras.layers.Dropout(0.2),
  # Camada de saída - como são de 0 a 9 serão 10 saídas
  tf.keras.layers.Dense(10, activation='softmax')

])

# Definir algoritmo de treinamento, função de perda e a métrica de treinamento
model.compile(optimizer='adam',

              loss='sparse_categorical_crossentropy',

              metrics=['accuracy'])

# Treinar a rede
history = model.fit(x_train, y_train, epochs=200)
# Avaliar a acurácia de rede no conjunto de teste
model.evaluate(x_test,  y_test, verbose=2)

# Plot das figuras com acurácia e perda
plt.plot(history.history['accuracy'])
plt.title('Acurácia do Modelo')
plt.ylabel('Acurácia')
plt.xlabel('Época')
plt.legend(['Treinamento'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.title('Perda do Modelo')
plt.ylabel('Perda')
plt.xlabel('Época')
plt.legend(['Treinamento'], loc='upper right')

plt.show()