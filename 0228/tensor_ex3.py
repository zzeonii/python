import tensorflow as tf
import numpy as np

X=np.array([[2,3]])
YT=np.array([[27,-30]])
W=np.array([[3,5],[4,6]])
B=np.array([1,2])

model=tf.keras.Sequential([
    tf.keras.Input(shape=(2,)),
    tf.keras.layers.Dense(2, activation='relu'),
    tf.keras.layers.Dense(2, activation='sigmoid')
])
model.layers[0].set_weights([W,B])
model.compile(loss='mse', optimizer='sgd')
Y=model.predict(X)
print(Y)

model.fit(X,YT,epochs=1000)
print('W=',model.layers[0].get_weights()[0])
print('B=',model.layers[0].get_weights()[1])
Y=model.predict(X)
print(Y)
