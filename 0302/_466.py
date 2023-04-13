import tensorflow as tf
import numpy as np

mnist=tf.keras.datasets.mnist

(X,YT),(x,yt)=mnist.load_data()

X,x=X/255, x/255
X,x=X.reshape((60000,784)),x.reshape((10000,784))

model=tf.keras.Sequential([
    tf.keras.Input(shape=(784,)),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dense(10,activation='linear')
])

model.compile(optimizer='adam',
              loss='mse',
              metrics=['accuracy'])

model.fit(X,YT,epochs=5)

model.evaluate(x,yt)