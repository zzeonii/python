import tensorflow as tf

mnist=tf.keras.datasets.mnist

(_,_),(x,yt)=mnist.load_data()

x=x/255
x=x.reshape((10000,784))

model=tf.keras.models.load_model('model.h5')

y=model.predict(x[0:1])
print(y[0],yt[0])

import numpy as np
print(np.argmax(y[0]))