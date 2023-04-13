"4*4 스트라이드stride"

>>> import numpy as np
>>> np.random.seed(1)
>>> image=np.random.randint(5,size=(4,4))
>>> image
array([[3, 4, 0, 1],
       [3, 0, 0, 1],
       [4, 4, 1, 2],
       [4, 2, 4, 3]])
>>> filter=np.random.randint(5,size=(3,3))
>>> filter
array([[4, 2, 4],
       [2, 4, 1],
       [1, 0, 1]])
>>> convolution=np.zeros((2,2))
>>> 
>>> for row in range(2):
    for col in range(2):
        window=image[row:row+3, col:col+3]
        convolution[row,col]=np.sum(window*filter)
        
>>> convolution
array([[31., 27.],
       [45., 23.]])
>>> 
