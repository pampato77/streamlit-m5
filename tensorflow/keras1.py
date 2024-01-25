from tensorflow import keras
from tensorflow.keras import layers

# y = wx + b
# create a neural network with 1 linear unit

model = keras.Sequential([
      layers.Dense(units=1, input_shape=[1]),
      ])

print(model.summary())
w, b = model.weights
print(w)
print(b)

