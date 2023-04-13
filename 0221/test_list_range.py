>>> test_list=['one','two','three']
>>> for i in test_list:
    print(i)
   
one
two
three

>>> range(0,10)
range(0, 10)
>>> a=range(10)
>>> a
range(0, 10)
>>> [*a]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> b=range(0,10,2)
>>> c=range(10,0,-2)
>>> [*b]
[0, 2, 4, 6, 8]
>>> [*c]
[10, 8, 6, 4, 2]
>>> *b,
(0, 2, 4, 6, 8)
>>> *c,
(10, 8, 6, 4, 2)