>>> a=[1,2,3,4,5]
>>> b=a[:2]
>>> c=a[2:]
>>> b
[1, 2]
>>> c
[3, 4, 5]
>>> a[0:2]
[1, 2]
>>> b[0:2]
[1, 2]
>>> c[0:2]
[3, 4]
>>> a=b
>>> a+b
[1, 2, 1, 2]
>>> a+c
[1, 2, 3, 4, 5]
>>> a*c
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'list'
>>> c*3
[3, 4, 5, 3, 4, 5, 3, 4, 5]
>>> a*7
[1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
>>> A=[1,2,3,4,5]
>>> a[1:3]
[2]
>>> A[1:3]
[2, 3]
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> a+b
[1, 2, 3, 4, 5, 6]
>>> *a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: MainCPythonBackend._install_repl_helper.<locals>._handle_repl_value() takes 1 positional argument but 3 were given
>>> [*a]
[1, 2, 3]
>>> [*a,*b]
[1, 2, 3, 4, 5, 6]
>>> [*a+b]
[1, 2, 3, 4, 5, 6]
>>> a[:2]
[1, 2]
>>> [*a[:2],*b[2:]]
[1, 2, 6]
>>> [*a[0:1]]
[1]
>>> a[0]
1
>>> a[:1]
[1]
>>> [*a[:1]]
[1]
>>> a=[1,2,3]
>>> len(a)
3
>>> len()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: len() takes exactly one argument (0 given)
>>> a
[1, 2, 3]
>>> b=[5,6,7,8,9]
>>> b
[5, 6, 7, 8, 9]
>>> len(a+b)
8
>>> a
[1, 2, 3]
>>> a[2]=4
>>> a
[1, 2, 4]
>>> a
[1, 2, 4]
>>> del a[1]
>>> a
[1, 4]
>>> a=[1,2,3,4,5]
>>> del a[2:]
>>> a
[1, 2]
>>>  a=[1,2,3]
>>> a.append(4)
>>> a
[1, 2, 3, 4]
>>> a.append([5,6])
>>> a
[1, 2, 3, 4, [5, 6]]
>>> a=[7,2,8,4,6]
>>> a.sort()
>>> a
[2, 4, 6, 7, 8]
>>> b=['l','e','k','t']
>>> b.sort()
>>> b
['e', 'k', 'l', 't']
>>> c=['l','k','t','e','j','p']
>>> c.sort()
>>> c
['e', 'j', 'k', 'l', 'p', 't']
>>> d=['ㅌ','ㄱ','ㅈ','ㅇ']
>>> d.sort()
>>> d
['ㄱ', 'ㅇ', 'ㅈ', 'ㅌ']
>>> a=['a','c','b']
>>> a.reverse()
>>> a
['b', 'c', 'a']
>>> a=[1,2,3,4,5]
>>> a.index(5)
4
>>> a.index(6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 6 is not in list
>>> 
>>> a=['a','c','b']
>>> ar=a[::-1]
>>> ar
['b', 'c', 'a']
>>> a.sort()
>>> a
['a', 'b', 'c']
>>> a.reverse()
>>> a
['c', 'b', 'a']
>>> import random
>>> random.shuffle(a)
>>> a
['b', 'c', 'a']
>>> 
>>> a=[1,2,3]
>>> a.pop()
3
>>> a
[1, 2]
>>> a=[1,2,3,4,1]
>>> a.count(1)
2
>>> a.count(4)
1
>>> 