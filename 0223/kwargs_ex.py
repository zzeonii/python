>>> def print_kwargs(**kwargs):
    kwargs
    
>>> print_kwargs(a=1)
{'a': 1}
>>> print_kwargs(a=1,b=2)
{'a': 1, 'b': 2}
>>> print_kwargs(**{'a': 1, 'b': 2})
{'a': 1, 'b': 2}
>>> D={'a': 1, 'b': 2}
>>> print_kwargs(**D)
{'a': 1, 'b': 2}
>>> samsung={'name':'삼성전자', 'code':'002325'}
>>> lg={'name':'LG전자', 'code':'113532'}
>>> 
>>> print_kwargs(**samsung)
{'name': '삼성전자', 'code': '002325'}
>>> print_kwargs(**lg)
{'name': 'LG전자', 'code': '113532'}
>>> 
