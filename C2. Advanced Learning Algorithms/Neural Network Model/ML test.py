import numpy as np
import tensorflow as tf
X = np.array[[200, 17]]
layer_1 = tf.keras.layers.dense(units = 3, activation = "sigmoid")
a1 = layer_1(X)
layer_2 = tf.keras.layers.dense(units = 1, activation = "sigmoid")
a2 = layer_2(a1)
if a2 >= 0.5:
    yhat = 1
else:
    yhat = 0