>>> import numpy as np
>>> np.random.seed(1)
>>> image=np.random.randint(5,size=(4,4))
>>> filter=np.random.randint(5,size=(3,3))
>>> image_pad=np.pad(image,((1,1),(1,1)))
>>> convolution=np.zeros((4,4))
>>> for row in range(4):
     for col in range(4):
            window=image_pad[row:row+3,col:col+3]
            convolution[row,col]=np.sum(window*filter)
                         
>>> max_pooled=np.zeros((2,2))
>>> for row in range(0,2):
    for col in range(0,2):
            window=convolution[2*row:2*row+2,2*col:2*col+2]
            max_pooled[row,col]=np.max(window)
                         
>>> max_pooled
array([[38., 27.],
       [48., 49.]])