#튜플(tuple), 사전(dictionary), 집합(set) 소개
>>> t=(1,2,3,4)
>>> d={'a':1,'b':2,'c':3,'d':4}
>>> s={1,2,2,3,3,3,4,4,4}
>>> t
(1, 2, 3, 4)
>>> d
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> s
{1, 2, 3, 4}
>>> type(t)
<class 'tuple'>
>>> type(d)
<class 'dict'>
>>> type(s)
<class 'set'>
>>> for i in t:
    i
    
1
2
3
4
>>> for i in d:
    i
    
'a'
'b'
'c'
'd'
>>> for i in s:
    i
    
1
2
3
4

#튜플, 사전, 집합 : 내포와 생성자
>>> 
>>> t=(i for i in range(10))
>>> d={('key'+str(i)):i for i in range(10)}
>>> d
{'key0': 0, 'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5, 'key6': 6, 'key7': 7, 'key8': 8, 'key9': 9}
>>> t=(i for i in range(10))
>>> d={('key'+str(i)):i for i in range(10)}
>>> s={i for i in range(10)}
>>> t
<generator object <genexpr> at 0x0000024B8A113BC0>
>>> d
{'key0': 0, 'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5, 'key6': 6, 'key7': 7, 'key8': 8, 'key9': 9}
>>> s
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> type(t)
<class 'generator'>
>>> type(d)
<class 'dict'>
>>> type(s)
<class 'set'>
>>> for i in t:
    i
    
0
1
2
3
4
5
6
7
8
9

>>> for i in t:
    i
#generator는 1회용!!!!!!!!!!    
>>>
>>> for i in d:
    i
    
'key0'
'key1'
'key2'
'key3'
'key4'
'key5'
'key6'
'key7'
'key8'
'key9'
>>> for i in d:
    i
    
'key0'
'key1'
'key2'
'key3'
'key4'
'key5'
'key6'
'key7'
'key8'
'key9'
>>> for i in s:
    i
    
0
1
2
3
4
5
6
7
8
9
>>> 
