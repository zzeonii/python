>>> int_list=[]
>>> for i in range(10):
    int_list.append(i)
    
>>> int_list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> [i for i in range(10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> int_list_2=[i for i in range(10)]
>>> int_list_2
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> for i in range(5):
    i**2
    
0
1
4
9
16

>>> [i**2 for i in range(5)]
[0, 1, 4, 9, 16]
>>>

>>> for i in range(5):
    i**2+i
    
0
2
6
12
20
>>> [i**2+i for i in range(5)]
[0, 2, 6, 12, 20]
>>> (i**2+i for i in range(5))
<generator object <genexpr> at 0x000002349253A500>
>>> [*(i**2+i for i in range(5))]
[0, 2, 6, 12, 20]
>>> list((i**2+i for i in range(5)))
[0, 2, 6, 12, 20]