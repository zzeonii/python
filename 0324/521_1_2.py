import tensorflow as tf

mnist=tf.keras.datasets.cifar10

(x_train,y_train),(x_test,y_test)=mnist.load_data()
x_train,x_test=x_train/255,x_test/255

model=tf.keras.Sequential([
    tf.keras.layers.InputLayer(input_shape=x_train.shape[1:]),
    tf.keras.layers.Conv2D(24,(5,5),(2,2),activation='relu',padding='same'),
    tf.keras.layers.Conv2D(36,(5,5),(2,2),activation='relu',padding='same'),
    tf.keras.layers.Conv2D(48,(5,5),(2,1),activation='relu',padding='same'),
    tf.keras.layers.Conv2D(64,(3,3),(1,1),activation='relu',padding='same'),
    tf.keras.layers.Conv2D(64,(3,3),(1,1),activation='relu',padding='same'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(100,activation='relu'),
    tf.keras.layers.Dense(50,activation='relu'),
    tf.keras.layers.Dense(10,activation='relu'),
    tf.keras.layers.Dense(10,activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
    