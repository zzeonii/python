"3*3커널 사이즈"
>>> import numpy as np
>>> np.random.seed(1)
>>> image=np.random.randint(5, size=(3,3))
>>> image
array([[3, 4, 0],
       [1, 3, 0],
       [0, 1, 4]])
>>> filter=np.random.randint(5, size=(3,3))
>>> filter
array([[4, 1, 2],
       [4, 2, 4],
       [3, 4, 2]])
>>> image_x_filter=image*filter
>>> image_x_filter
array([[12,  4,  0],
       [ 4,  6,  0],
       [ 0,  4,  8]])
>>> convolution=np.sum(image_x_filter)
>>> convolution
38
>>