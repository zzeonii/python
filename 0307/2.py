>>> L=[1,2,3,4]
>>> def f(*args): #만능튜플(주머니)
    args
    
>>> f(L)
([1, 2, 3, 4],)
>>> f(L,L)
([1, 2, 3, 4], [1, 2, 3, 4])
>>> f(*L) #만능열쇠
(1, 2, 3, 4)
>>> 
