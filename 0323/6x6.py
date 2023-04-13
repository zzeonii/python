"6*6 패딩 padding"

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
>>> image_pad=np.pad(image,((1,1),(1,1)))
>>> image_pad
array([[0, 0, 0, 0, 0, 0],
       [0, 3, 4, 0, 1, 0],
       [0, 3, 0, 0, 1, 0],
       [0, 4, 4, 1, 2, 0],
       [0, 4, 2, 4, 3, 0],
       [0, 0, 0, 0, 0, 0]])
>>> convolution=np.zeros((4,4))
>>> for row in range(4):
    for col in range(4):
        window=image_pad[row:row+3, col:col+3]
        convolution[row,col]=np.sum(window*filter)
        
>>> convolution
array([[16., 25., 10.,  4.],
       [38., 31., 27.,  7.],
       [28., 45., 23., 16.],
       [42., 48., 49., 28.]])