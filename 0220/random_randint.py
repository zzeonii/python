>>> import random

random.random()

0.5354474356494815
>>> random.randint(0,100)
80
>>> float_list=[]
>>> for _ in range(10):
    float_list.append(random.random())
    
>>> float_list
[0.13422000785941657, 0.28967190782182894, 0.4616420745284515, 0.6854045683737966, 0.6423506932349281, 0.46038309460513194, 0.6768469150022247, 0.4776679906688831, 0.9882983809310621, 0.5533938168119109]
>>> 
>>> int_list_2=[]
>>> for _ in range(10):
    int_list_2.append(random.randint(0,100))
    
>>> int_list_2
[69, 20, 52, 18, 20, 94, 65, 43, 24, 30]
>>>
#리스트 내포
>>> [random.random() for _ in range(10)]
[0.9425444689099238, 0.5301210112160211, 0.11361895273560496, 0.6418515284988003, 0.051657871990752335, 0.9081853565626766, 0.7140023573545042, 0.9241665291155458, 0.402887872629759, 0.9280503735422433]
>>> [random.randint(0,100) for _ in range(10)]
[29, 3, 15, 35, 13, 45, 100, 20, 33, 30]
>>> float_list=[random.random() for _ in range(10)]
>>> float_list
[0.09114248874236641, 0.9957886883849884, 0.9529274854399457, 0.03616400494926064, 0.06739308780221187, 0.984305406369129, 0.87960565106227, 0.31288085332191695, 0.8955623923561281, 0.04287489535747935]
>>> int_list=[random.randint(0,100) for _ in range(10)]
>>> int_list
[6, 0, 35, 94, 63, 64, 70, 35, 75, 25]
>>> 
