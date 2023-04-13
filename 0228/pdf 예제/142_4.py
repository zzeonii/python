import tensorflow as tf

mnist=tf.keras.datasets.mnist

(X,YT),(x,yt)=mnist.load_data()
print(X.shape,YT.shape,x.shape,yt.shape)

import matplotlib.pyplot as plt

plt.imshow(X[0])
plt.show()

print(YT[0])
print(tf.one_hot(YT[0],10))

for row in range(28):
    for col in range(28):
        print('%4s' %X[0][row][col],end='')
    print()
    
import numpy as np

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(X[i],cmap=plt.cm.binary)
    plt.xlabel(YT[i])
plt.show()
