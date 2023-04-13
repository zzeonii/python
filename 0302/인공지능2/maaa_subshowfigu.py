import tensorflow as tf

mnist=tf.keras.datasets.fashion_mnist
# mnist=tf.keras.datasets.cifar10

(X,YT),(x,yt)=mnist.load_data()
print(X.shape,YT.shape,x.shape,yt.shape)

import matplotlib.pyplot as plt
# plt.imshow(X[3])
# plt.show()

print(YT[0])
print(max(YT))
# print(tf.one_hot(YT[0],100))

# for row in range(28):
#     for col in range(28):
#         print('%4s' %X[0][row][col],end='')
#     print()
    
plt.figure(figsize=(10,10))
for i in range(200):
    plt.subplot(10,20,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(X[i])
    plt.xlabel(YT[i])
plt.show()