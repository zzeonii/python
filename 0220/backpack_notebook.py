>>> backpack=['book','note book','tablet','pencil case']
>>> if 'note book' in backpack:
    where=backpack.index('note book')
    where
    notebook = backpack.pop(where)  #가방에서 노트북 꺼내기
    notebook
    
1
'note book'

>>> backpack
['book', 'tablet', 'pencil case']

#가방에 노트북 원래자리에 다시 넣기
>>> backpack.insert(1,'note book') #backpack.insert(where,notebook)
>>> backpack
['book', 'note book', 'tablet', 'pencil case']
>>> 
