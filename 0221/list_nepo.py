>>> a=[1,2,3,4]
>>> result=[]
>>> for num in a:
    result.append(num*3)
    
>>> print(result)
[3, 6, 9, 12]


>>> [(num*3) for num in a]
[3, 6, 9, 12]

>>> a=[1,2,3,4]
>>> result=[num * 3 for num in a]
>>> print(result)
[3, 6, 9, 12]

>>> 
>>> a=[1,2,3,4]
>>> result=[num * 3 for num in a if num % 2 == 0]
>>> print(result)
[6, 12]
>>> 
>>> for i in range(1,5):
    if i%2==0:
        i*3
        
6
12


>>> [i*3 for i in range(1,5) if i%2==0]
[6, 12]
>>> result=[x*y for x in range(2,10)
    for y in range(1,10)]
>>> print(result)
[2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24, 27, 4, 8, 12, 16, 20, 24, 28, 32, 36, 5, 10, 15, 20, 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42, 48, 54, 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 64, 72, 9, 18, 27, 36, 45, 54, 63, 72, 81]

>>> [i*3 for i in range(1,5) if i%2==0] #리스트
[6, 12]
>>> *(i*3 for i in range(1,5) if i%2==0), #튜플
(6, 12)

