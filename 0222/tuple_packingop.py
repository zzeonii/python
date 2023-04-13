
>>> a=(1,2,3,4)
>>> a
(1, 2, 3, 4)
>>> type(a)
<class 'tuple'>
>>> b=(1)
>>> b
1
>>> type(b)
<class 'int'>
>>> c=(1,)
>>> type(c)
<class 'tuple'>
>>> d,e=5,6
>>> d
5
>>> e
6
>>> d,e=(5,6)
>>> d
5
>>> e
6
>>> (d,e)=5,6
>>> d
5
>>> (d,e)=(5,6)
>>> d
5
>>> e
6
>>> 
>>> d,e=5,6,7
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
>>> d,*e=5,6,7
>>> d
5
>>> e
[6, 7]
>>> d,*e,f=5,6,7
>>> e
[6]
>>> d,*e,f=5,6,7,8
>>> e
[6, 7]
>>> d,*e,f=5,6
>>> e
[]
>>> d,*e,f=5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot unpack non-iterable int object
>>> *e,f=5,6
>>> e
[5]
>>> *e,=5,
>>> e
[5]
>>> *e=5,
Traceback (most recent call last):
  File "<stdin>", line 1
SyntaxError: starred assignment target must be in a list or tuple
>>> *e=5
Traceback (most recent call last):
  File "<stdin>", line 1
SyntaxError: starred assignment target must be in a list or tuple
>>> def g(*args):
    args
    
>>> g(1,2,3,4,5,6,7)
(1, 2, 3, 4, 5, 6, 7)
>>> *args,=1,2,3,4,5,6,7
>>> args
[1, 2, 3, 4, 5, 6, 7]
>>> g(1)
(1,)
>>> 
