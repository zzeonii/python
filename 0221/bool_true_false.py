# ﻿참(True)과 거짓(False)을 나타내는 자료형
# 변수 지정
>>> a=True
>>> b=False
#type()함수를 사용하여 자료형 확인
>>> type(a)
<class 'bool'>
>>> type(b)
<class 'bool'>
#조건문의 반환 값으로도 사용됨
>>> 1==1
True
>>> 2>1
True
>>> 2<1
False
>>> 
# 문자열의 참/거짓
>>> bool('python')
True
>>> bool()
False
# 리스트의 참/거짓
>>> bool([1,2,3])
True
>>> bool([])
False
# 숫자의 참/거짓
>>> bool(0)
False
>>> bool(3)
True