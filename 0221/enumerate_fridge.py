>>> import numpy as np
>>> np.random.randint(0,100,10)
array([28, 91, 48, 83, 78, 82, 58, 90, 68,  0])
>>> [*np.random.randint(0,100,10)]
[98, 92, 86, 60, 2, 15, 21, 20, 34, 48]
>>> *np.random.randint(0,100,10),
(47, 52, 5, 50, 70, 94, 59, 47, 21, 77)
>>> for i in np.random.randint(0,100,10):
    i
    
3
18
94
57
22
39
77
51
40
0
>>> 
>>> fridge=['apple','straw berry','mange']
>>> for i in enumerate(fridge): #교재 234페이지 참고
    i
    
(0, 'apple')
(1, 'straw berry')
(2, 'mange')
>>> enumerate(fridge)
<enumerate object at 0x00000276A676FAC0>
>>> [*enumerate(fridge)]
[(0, 'apple'), (1, 'straw berry'), (2, 'mange')]
>>> 
