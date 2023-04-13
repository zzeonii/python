import tensorflow as tf

mnist = tf.keras.datasets.mnist

(X, YT), (x, yt) = mnist.load_data()
print(X.shape, YT.shape, x.shape, yt.shape)

#pip3 install matplotlib
# from matplotlib import pyplot as plt
# plt.imshow(X[1])
# plt.show()
print(YT[0:3])
print(tf.one_hot(YT[0:3],10))
# X,x=X/255, x/255
# X,x=X.reshape((60000,784)),x.reshape((10000,784))

model=tf.keras.Sequential([
    tf.keras.Input(shape=(784,)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(X,YT,epochs=5)

model.evaluate(x,yt)



