import tensorflow as tf

mnist=tf.keras.datasets.fashion_mnist

(X,YT),(x,yt)=mnist.load_data()
X,x=X/255,x/255
X=X.reshape((60000,28,28,1))
x=x.reshape((10000,28,28,1))

model=tf.keras.Sequential([
    tf.keras.Input(shape=(28,28,1)),
    tf.keras.layers.Conv2D(32,(3,3),activation='relu'),
    tf.keras.layers.Conv2D(64,(3,3),activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dense(10,activation='softmax')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(X,YT,epochs=5)
model.evaluate(x,yt)