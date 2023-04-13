import tensorflow as tf

mnist=tf.keras.datasets.mnist

(X,YT),(x,yt)=mnist.load_data()

print(YT[0])
print(YT[:10])
print(tf.one_hot(YT[0],10))
print(tf.one_hot(YT[1],10))
print(tf.one_hot(YT[2],10))
print(tf.one_hot(YT[2],10).numpy())

print(tf.one_hot(YT[:10],10).numpy())
import numpy as np
print(np.argmax(tf.one_hot(YT[2],10)))

# 
# X,x=X/255,x/255
# X,x=X.reshape((60000,28*28)),x.reshape((10000,28*28))
# 
# model=tf.keras.Sequential([
#     tf.keras.Input(shape=(28*28,)),
#     tf.keras.layers.Dense(128,activation='relu'),
#     tf.keras.layers.Dense(10,activation='softmax')
# ])
# model.compile(optimi
#               zer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])
# model.fit(X,YT,epochs=5)
# model.evaluate(x,yt)
# 