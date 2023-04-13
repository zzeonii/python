>>> (i for i in range(5))
<generator object <genexpr> at 0x000001F7597ACB30>
>>> [*(i for i in range(5))]
[0, 1, 2, 3, 4]
>>> type({})
<class 'dict'>
>>> len({})
0
>>> fridge={'apple':2,'banana':5,'orange':10}
>>> for fruit,howmany in fridge.items():
    fruit, howmany
    
('apple', 2)
('banana', 5)
('orange', 10)
>>> for item in fridge.items():
    item
    
('apple', 2)
('banana', 5)
('orange', 10)
>>> for item in fridge.keys():
    item
    
'apple'
'banana'
'orange'
>>> for item in fridge.values():
    item
    
2
5
10
>>> for item in fridge:
    item
    
'apple'
'banana'
'orange'
>>> for item in fridge.items():
    item
    
('apple', 2)
('banana', 5)
('orange', 10)
>>> [*fridge]
['apple', 'banana', 'orange']
>>> fridge.keys()
dict_keys(['apple', 'banana', 'orange'])
>>> type(fridge.keys())
<class 'dict_keys'>
>>> [*fridge.keys()]
['apple', 'banana', 'orange']
>>> list[fridge.keys()]
list[dict_keys(['apple', 'banana', 'orange'])]
>>> fridge.values()
dict_values([2, 5, 10])
>>> type(fridge.values())
<class 'dict_values'>
>>> [*fridge.values()]
[2, 5, 10]
>>> type(fridge.items())
<class 'dict_items'>
>>> [*fridge.items()]
[('apple', 2), ('banana', 5), ('orange', 10)]
>>> 
