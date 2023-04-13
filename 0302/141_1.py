import tensorflow as tf

mnist = tf.keras.datasets.mnist

(X, YT), (x, yt) = mnist.load_data() #60000개의 학습데이터, 10000개의 검증데이터

X, x = X/255, x/255 # 60000x28x28, 10000x28x28
X, x = X.reshape((60000,784)), x.reshape((10000,784))

model = tf.keras.Sequential([
    tf.keras.Input(shape=(784,)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
]) # 신경망 모양 결정(W, B 내부적 준비)

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X,YT,epochs=5)

model.evaluate(x,yt)