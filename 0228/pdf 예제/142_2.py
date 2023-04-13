import tensorflow as tf

mnist=tf.keras.datasets.mnist

(X,YT),(x,yt)=mnist.load_data()
print(X.shape,YT.shape,x.shape,yt.shape)

import matplotlib.pyplot as plt

plt.imshow(X[0])
plt.show()

print(YT[0])
print(tf.one_hot(YT[0],10))
