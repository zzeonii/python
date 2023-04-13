>>> def say():
    word=input('say something: ')
    return word

>>> say()
say something: hi
'hi'
>>> def get_order():
    order=input('what do you want? coffee or tea? ')
    return order

>>> get_order()
what do you want? coffee or tea? coffee
'coffee'
>>> def add(a,b):
    print("%d, %d의 합은 %d입니다.: %(a,b,a+b))
    
  File "<stdin>", line 2
    print("%d, %d의 합은 %d입니다.: %(a,b,a+b))
          ^
SyntaxError: unterminated string literal (detected at line 2)
>>> def add(a,b):
    print("%d, %d의 합은 %d입니다.: "%(a,b,a+b))
    
>>> 
>>> add(7,8)
7, 8의 합은 15입니다.: 
>>> def add(a,b):
    print("%d, %d의 합은 %d입니다. "%(a,b,a+b))
    
>>> add(3,4)
3, 4의 합은 7입니다. 
>>> result=add(a=3,b=7)
3, 7의 합은 10입니다. 
>>> def add(a,b):
    return a+b

>>> result = add(a=3,b=7)
>>> print(result)
10
>>> result=add(b=5,a=3)
>>> print(result)
8
>>> 
