import tensorflow as tf
import numpy as np

mnist=tf.keras.datasets.mnist

(X,YT),(x,yt)=mnist.load_data()

X,x=X/255, x/255
YT,yt=YT/9,yt/9
X,x=X.reshape((60000,784)),x.reshape((10000,784))

model=tf.keras.Sequential([
    tf.keras.Input(shape=(784,)),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dense(1,activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='mse')

model.fit(X,YT,epochs=50)

model.evaluate(x,yt)