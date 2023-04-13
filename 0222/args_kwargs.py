# *args 인자 이해하기

>>> def f(*args):
    args
    
>>> f(1)
(1,)
>>> f(1,2)
(1, 2)
>>> f(1,2,3)
(1, 2, 3)
>>> L=[1,2,3,4]
>>> f(*L)
(1, 2, 3, 4)
>>>


# **kwargs
 
>>> def g(**kwargs):
    kwargs
    
>>> g(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: g() takes 0 positional arguments but 1 was given
>>> g(a=1)
{'a': 1}
>>> g(a=1,2)
  File "<stdin>", line 1
    g(a=1,2)
           ^
SyntaxError: positional argument follows keyword argument
>>> g(a=1,b=2)
{'a': 1, 'b': 2}
>>> D={'a':1,'b':2,'c':3}
>>> g(**D)
{'a': 1, 'b': 2, 'c': 3}
>>> 
