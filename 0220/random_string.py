>>> import random
>>> import string
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> random.choices(string.ascii_letters, k=10)
['H', 'Z', 'x', 'w', 'i', 'D', 'o', 'f', 'F', 'V']
>>> ''.join(random.choices(string.ascii_letters, k=10))
'hVLIqXGBbB'
>>> str_list=[]
>>> for _ in range(10):
    str_list.append(''.join(random.choices(string.ascii_letters, k=10)))
    
>>> str_list
['UmrJmMyeKv', 'KAzjWgVYwt', 'GueZuAFYQY', 'NlqhegYVAi', 'HafLVXgFAH', 'iogBpDoMbf', 'DYcJQIYIhh', 'cifplNeqsC', 'zZbkYtvEDj', 'ZYjsjUZPNt']


#리스트 내포
>>> [''.join(random.choices(string.ascii_letters, k=10)) for _ in range(10)]
['yYDIKKhSUx', 'ZoTDtMsyhk', 'wWzdzifpNh', 'urqYkIRTUW', 'PHmvNhcskw', 'uuwoWCKWOa', 'ySyJrFYMIh', 'pjPNZBaEBV', 'YVXoOpCqiy', 'qlPilzrpni']
>>> 
>>> str_list_2=[''.join(random.choices(string.ascii_letters, k=10)) for _ in range(10)]
>>> str_list_2
['WvxtFFsxcu', 'JXSCIycdLm', 'mKManmozCy', 'pqUiRZSfvu', 'dVJYLSRxzb', 'XoTyYmpatu', 'MmTiJkOJiO', 'ZasMLcTrYx', 'RvoWPuNJxP', 'BFiqjylMPf']