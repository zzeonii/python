import tensorflow as tf
from _7seg_data import X

model=tf.keras.models.load_model("model.h5")

x=X[:1]
print(x.shape)

Y=model.predict(x)
print(Y)
