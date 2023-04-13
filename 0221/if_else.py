Python 3.10.9 (C:\Program Files (x86)\Thonny\python.exe)
>>> #돈이 있으면 택시를 타고, 돈이 없으면 걸어간다
>>> money=True
>>> if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
    
택시를 타고 가라
>>> pocket=['paper','cellphone']
>>> card=True
>>> if 'money' in pocket:
    print('택시를 타고 가라')
else :
    if card:
        print('택시를 타고 가라')
    else:
        print('걸어가라')
        
택시를 타고 가라
>>> 
>>> pocket=['paper','cellphone']
>>> card=True
>>> if 'money' in pocket:
    print('택시를 타고 가라')
elif card:
    print('택시를 타고 가라')
else:
    print('걸어가라')
    
택시를 타고 가라
>>> 
