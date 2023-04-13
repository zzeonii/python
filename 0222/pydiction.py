#파이썬 딕셔너리
>>> scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
>>> *a,b,c=scores
>>> a
[8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5]
>>> b
7.8
>>> c
9.4
>>> 
>>> scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _= scores
print(valid_score)
[8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5]
>>> scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
>>> _,_,*valid_score=scores
>>> pring
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pring' is not defined
>>> 
>>> print(valid_score)
[8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
>>> temp={}
>>> print(temp)
{}
>>> ice={'메로나':1000,'폴라포':1200,'빵빠레':1800}
>>> ice
{'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}
>>> ice['죠스바']=1200
>>> ㅑㅊㄷ
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ᅣᄎᄃ' is not defined
>>> ice
{'메로나': 1000, '폴라포': 1200, '빵빠레': 1800, '죠스바': 1200}
>>> ice['월드콘']=1500
>>> ice
{'메로나': 1000, '폴라포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
>>> ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
>>> grade['메로나']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'grade' is not defined
>>> print(ice)
{'메로나': 1000, '폴로포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
>>> print("메로나 가격 : ", ice['메로나'])
메로나 가격 :  1000
>>> ice('죠스바')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict' object is not callable
>>> print(ice['죠스바'])
1200
>>> ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
>>> ice['메로나']=1300
>>> print(ice)
{'메로나': 1300, '폴로포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
>>> ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
>>> del ice['메로나']
>>> print(ice)
{'폴로포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
>>> inventory={"메로나": [300, 20], 
             "비비빅": [400, 3], 
             "죠스바": [250, 100]}
>>> print(inventory)
{'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100]}
>>> inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
>>> print(inventory["메로나"])
[300, 20]
>>> print(inventory["메로나"][0])
300
>>> print(inventory["메로나"][ㅂ])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ᄇ' is not defined
>>> print(inventory["메로나"][1])
20
>>> inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
>>> inventory["월드콘"]=[500,7]
>>> print(inventory)
{'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100], '월드콘': [500, 7]}
>>> icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
>>> icecream.keys()
dict_keys(['탱크보이', '폴라포', '빵빠레', '월드콘', '메로나'])
>>> icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
>>> ice=list(icecream.values())
>>> print(ice)
[1200, 1200, 1800, 1500, 1000]
>>> icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
>>> print(sum(icecream.values()))
6700
>>> icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
>>> icecream+new_product
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> ice=icecream
>>> np=newproduct
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'newproduct' is not defined
>>> np=new_product
>>> ice{}+np{}
  File "<stdin>", line 1
    ice{}+np{}
       ^
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
>>> icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
>>> icecream.update(new_product)
>>> icecream
{'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000, '팥빙수': 2700, '아맛나': 1000}
>>> keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
>>> keys.zip(vals)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'zip'
>>> keys=zip(vals)
>>> keys
<zip object at 0x0000021CD1E0DCC0>
>>> print(keys)
<zip object at 0x0000021CD1E0DCC0>
>>> print(*keys)
(300,) (250,) (400,)
>>> keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
>>> z=zip(keys,vals)
>>> print(z)
<zip object at 0x0000021CD1E0F580>
>>> print([*z])
[('apple', 300), ('pear', 250), ('peach', 400)]
>>> keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
>>> result=dict(zip(keys,vals))
>>> print(result)
{'apple': 300, 'pear': 250, 'peach': 400}
>>> result=zip(keys,vals)
>>> print(result)
<zip object at 0x0000021CD1E0EB00>

>>> date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
>>> close_table=dict(zip(date,close_price))
>>> print(close_table)
{'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}
>>> 