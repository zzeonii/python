#딕셔너리

>>> dic={'name':'EJ','phone':'01025802580','birth':'0526'}
>>> 
>>> dic
{'name': 'EJ', 'phone': '01025802580', 'birth': '0526'}

>>> dic['name']
'EJ'
>>> grade={'pey':10,'줄리엣':99}
>>> grade['줄리엣']
99
>>> a={1:'a'}
>>> a[2]='b'
>>> a
{1: 'a', 2: 'b'}
>>> del a[1]
>>> a
{2: 'b'}
>>> a.keys
<built-in method keys of dict object at 0x000001F75960B440>
>>> a.keys()
dict_keys([2])

>>> dic.keys()
dict_keys(['name', 'phone', 'birth'])
>>> 
>>> 
>>> 
>>> 
>>> dic={'name':'EJ','phone':'01025802580','birth':'0526'}
>>> a={'name':'EJ','phone':'01025802580','birth':'0526'}
>>> a.keys()
dict_keys(['name', 'phone', 'birth'])
>>> for k in a.keys():
    print(k)
    
name
phone
birth
>>> list(a.keys())
['name', 'phone', 'birth']
>>> a.values()
dict_values(['EJ', '01025802580', '0526'])
>>> a.items()
dict_items([('name', 'EJ'), ('phone', '01025802580'), ('birth', '0526')])
>>> [*a.items()]
[('name', 'EJ'), ('phone', '01025802580'), ('birth', '0526')]
>>> 
