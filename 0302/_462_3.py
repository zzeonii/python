import tensorflow as tf
from _7seg_data import X,YT

model=tf.keras.models.load_model("model.h5")

Y=model.predict(X)
print(Y)