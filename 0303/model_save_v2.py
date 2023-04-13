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

 
# X,x=X/255,x/255
# X,x=X.reshape((60000,784)),x.reshape((10000,784))
# 
# model=tf.keras.Sequential([
# np.set_printoptions(precision=3,suppress=True)
# y=model.predict(x[:1])
# print(y[0])
# print(yt[0])
# print(np.argmax(y[0]))