# adsoft 
import numpy as np
import os
#import matplotlib.pyplot as plt

# TensorFlow
import tensorflow as tf
 
print(tf.__version__)
# y = wX + b
X = np.arange(-10.0, 10.0, 1e-4)
#print(X)
np.random.shuffle(X)
#print('X =')
print(X)

# w = 3.1416
# b = 2.7

y =  3.1416 * X + 2.7
#print('y =')
#print(y)

train_end = int(0.6 * len(X))
#print (train_end)
test_start = int(0.8 * len(X))
#print (test_start)
X_train, y_train = X[:train_end], y[:train_end]
#print('train X, y', X_train, y_train)

X_test, y_test = X[test_start:], y[test_start:]
#print('test X, y', X_test, y_test)

X_val, y_val = X[train_end:test_start], y[train_end:test_start]
#print('Val X, y', X_val, y_val)


tf.keras.backend.clear_session()
linear_model = tf.keras.models.Sequential([
                                           tf.keras.layers.Dense(units=1, input_shape=[1], name='Single')
                                           ])
linear_model.compile(optimizer=tf.keras.optimizers.SGD(), loss=tf.keras.losses.mean_squared_error)
print(linear_model.summary())

w, b = linear_model.weights
print('w , b ', w, b)

linear_model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=20)

w, b = linear_model.weights
print('w , b ', w, b)

print(linear_model.predict([ [0.0], [1.0], [2.0], [3.0], [4.0] ] ).tolist() )   

export_path = 'linear-model/1/'
tf.saved_model.save(linear_model, os.path.join('./',export_path))
