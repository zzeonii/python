>>> def t_func():
    return 1,2,3

>>> a=t_func()

>>> a
(1, 2, 3)
>>> a,b,c=t_func()
>>> a
1
>>> b
2
>>> c
3
>>> a,*b=t_func()

>>> b
[2, 3]
>>> 
