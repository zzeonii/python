[[ input() 사용법 ]]
사용자가 입력한 값을 어떤 변수에 대입하고 싶을 때 사용
input()은 입력되는 모든 것을 문자열로 취급
프롬프트(>>>) 값을 띄워서 사용자 입력받기
 - 사용자에게 입력받을 때 안내 문구 또는 질문이 나오도록 하고 싶을 때
 
 
 >> a=input()
Life is too short, you need python
>>> a
'Life is too short, you need python'
>>> number=input("숫자를 입력하세요: ")
숫자를 입력하세요: 3


 [[ print()사용법 ]]
 입력한 자료형을 불러옴
 큰따옴표로 문자열 연결
 따옴표로 둘러싸인 문자열을 연속해서 쓰면 + 연산을 한 것과 동일
 문자열 띄어쓰기 : , 사용
 끝 문자 지정 : 매개변수 end를 사용해 끝 문자를 지정
 
 >>> number=input("숫자를 입력하세요: ")
숫자를 입력하세요: 3
>>> print(number)
3
>>> #print
>>> a=123
>>> print(a)
123
>>> a="Python"
>>> print(a)
Python
>>> a=[1,2,3]
>>> print(a)
[1, 2, 3]
>>> print("life""is""too short")
lifeistoo short
>>> print("life"+"is"+"too short")
lifeistoo short
>>> print("life","is","too short")
life is too short
>>> print('life''is''too short')
lifeistoo short
>>> print('life','is','too short')
life is too short
>>> print('a')
a
>>> print('a',end='\n')
a
>>> print('a',end=' ')
a 
>>> print('a',end='')
a
>>> print('a',end=':')
a:
>>> for i in range(10):
    print(i, end=' ')
    
0 1 2 3 4 5 6 7 8 9 
>>> for i in range(10):
    print(i, end='\n')
    
0
1
2
3
4
5
6
7
8
9
>>> for i in range(10):
    print(i, end='')
    
0123456789
>>> for i in range(10):
    print(i, end=':')
    
0:1:2:3:4:5:6:7:8:9:
>>> 
