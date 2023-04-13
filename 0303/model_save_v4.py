import tensorflow as tf
import numpy as np
mnist=tf.keras.datasets.cifar10
(X,YT),(x,yt)=mnist.load_data()
print(X.shape,YT.shape,x.shape,yt.shape)

import matplotlib.pyplot as plt
plt.imshow(X[0][:,:,2], cmap='Blues')
# plt.show()

for row in range(32):
    for col in range(32):
        print('%4d' %X[0][:,:,0][row][col],end='')
    print()
print(np.min(X),np.max(X))
X,x=X/255,x/255
X,x=X.reshape((50000,3072)),x.reshape((10000,3072))

model=tf.keras.Sequential([
    tf.keras.Input(shape=(3072,)),
    tf.keras.layers.Dense(1072,activation='relu'),
    tf.keras.layers.Dropout(0,2),
    tf.keras.layers.Dense(512,activation='relu'),
    tf.keras.layers.Dropout(0,2),
    tf.keras.layers.Dense(10,activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X,YT,epochs=5)

# model.evaluate(x,yt)
