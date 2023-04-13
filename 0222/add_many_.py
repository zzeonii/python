>>> def add_many(*args): #묶기 연산자
...     result=0
...     for i in args:
...             result += i
...     return result
...
>>> result=add_many(1,2,3)
>>> result
6
>>> result=add_many(1,2,3,4,5,6,7,8,9,10)
>>>
>>>
>>> rsss
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'rsss' is not defined
>>> result
55
>>> import numpy as np
>>> L=[*np.random.randint(1,100,1000)]
>>> L[:10]
[37, 66, 64, 89, 89, 82, 59, 95, 47, 66]
>>> result=add_many(*L)  #풀기 연산
>>> result
49671