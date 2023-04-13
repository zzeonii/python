>>> f= lambda a,b:a*b
>>> f(10,20)
200
>>> f2=lambda a:a**2
>>> f2(3)
9
>>> f3=lambda a:a>2
>>> f3(2)
False
>>> 
>>> 
>>> 
>>> f= lambda a,b:a*b
>>> f(10,20)
200
>>> m=map(lambda a:a**2,[1,2,3,4])
>>> m
<map object at 0x00000203C094DA80>
>>> m=[*m]
>>> m
[1, 4, 9, 16]
>>> f=lambda a:a**2
>>> l=[1,2,3,4]
>>> for m in map(f,l):
    m
    
1
4
9
16
>>> 
>>> f=filter(lambda a:a>2,[1,2,3,4])
>>> f
<filter object at 0x00000203C094CB20>
>>> f=[*f]
>>> f
[3, 4]
>>> f=lambda a:a>2
>>> l=[1,2,3,4]
>>> for f in filter(f,l):
    f
    
3
4
>>> 
