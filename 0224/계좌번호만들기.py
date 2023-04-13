>>> import random
>>> import string
>>> string.digits
'0123456789'
>>> random.choices(string.digits,k=3)
['0', '5', '9']
>>> random.choices(string.digits,k=2)
['4', '1']
>>> random.choices(string.digits,k=6)
['8', '0', '9', '8', '1', '0']
#계좌번호 만들기 1번
>>> first=''.join(random.choices(string.digits,k=3))
>>> mid=''.join(random.choices(string.digits,k=2))
>>> last=''.join(random.choices(string.digits,k=6))
>>> acc_num=first+'-'+mid+'-'+last
>>> acc_num
#계좌번호 만들기 2번
>>> first=random.randint(0,1000)
>>> mid=random.randint(0,100)
>>> last=random.randint(0,1000000)
>>> acc_num='%03d-%02d-%06d'%(first,mid,last)
>>> acc_num
#계좌번호 만들기 3번
>>> acc_num='{:03}-{:02}-{:06}'.format(first,mid,last)
>>> acc_num
#계좌번호 만들기 4번
>>> acc_num=f'{first:03}-{mid:02}-{last:06}'
>>> acc_num
'944-88-396319'
