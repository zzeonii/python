import tensorflow as tf

mnist=tf.keras.datasets.mnist

(_,_),(x,yt)=mnist.load_data()
x=x/255
x=x.reshape((10000,784))

model=tf.keras.models.load_model('손글씨_학습_인공지능.h5')

y=model.predict(x[:1])
print(y[0])