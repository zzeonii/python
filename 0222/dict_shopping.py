#dict : 열쇠로 값 찾기
#dict는 키와 값을 하나의 항목으로 하여 구성된 자료형
#{key1:value1, key2:value2, key3:value3,...}
#key는 문자열이나 정수
#value는 문자열, 정수, 실수, 또는 객체

# dict 생성
>>> shopping={}

>>> shopping['apple']=3
>>> shopping['pear']=2
>>> shopping['hanrabong']=5
>>> shopping['pine apple']=2
>>> shopping
{'apple': 3, 'pear': 2, 'hanrabong': 5, 'pine apple': 2}
>>>
#dict 항목 읽기
>>> shopping['apple']
3
>>> shopping['hanrabong']
5
# 없는 항목 찾을 시 오류 발생
>>> shopping['banana']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'banana'

>>> shopping={'apple': 3, 'pear': 2, 'hanrabong': 5, 'pine apple': 1}
>>> shopping.keys()
dict_keys(['apple', 'pear', 'hanrabong', 'pine apple'])
>>> shopping.values()
dict_values([3, 2, 5, 1])
>>> shopping.items() #항목 다 풀어보기
dict_items([('apple', 3), ('pear', 2), ('hanrabong', 5), ('pine apple', 1)])
>>> 
#unpacking operator 만능열쇠
>>> [*shopping.keys()]
['apple', 'pear', 'hanrabong', 'pine apple']
>>> [*shopping.values()]
[3, 2, 5, 1]
>>> [*shopping.items()]
[('apple', 3), ('pear', 2), ('hanrabong', 5), ('pine apple', 1)]
>>>
#for-in문 사용하기
>>> for key in shopping.keys():
    key
    
'apple'
'pear'
'hanrabong'
'pine apple'
>>> for value in shopping.values():
    value
    
3
2
5
1
>>> for item in shopping.items():
    item
    
('apple', 3)
('pear', 2)
('hanrabong', 5)
('pine apple', 1)