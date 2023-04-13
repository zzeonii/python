Python 3.10.9 (C:\Program Files (x86)\Thonny\python.exe)
#리스트 생성
>>> movie_rank=['닥터 스트레인지', '스플릿', '럭키']
#리스트 원소 추가
>>> movie_rank.append('배트맨')
>>> print(movie_rank)
['닥터 스트레인지', '스플릿', '럭키', '배트맨']
#원하는 위치에 원소 추가
>>> movie_rank.insert(1,'슈퍼맨')
>>> print(movie_rank)
['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
#리스트 원소 삭제
>>> movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
>>> del movie_rank[2:3]
>>> print(movie_rank)
['닥터 스트레인지', '슈퍼맨', '배트맨']
>>> movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
>>> del movie_rank[2:4]
>>> print(movie_rank)
['닥터 스트레인지', '슈퍼맨']
#리스트 원소 합치기
>>> lang1 = ["C", "C++", "JAVA"]
>>> lang2 = ["Python", "Go", "C#"]
>>> langs=lang1+lang2
>>> print(langs)
['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']
#리스트에서 최댓값, 최소값 구하기
>>> nums = [1, 2, 3, 4, 5, 6, 7]
>>> min(nums)
1
>>> max(nums)
7
>>> print('max: ', max(nums))
max:  7
>>> print('min: ', min(nums))
min:  1
#리스트의 합 출력
>>> nums = [1, 2, 3, 4, 5]
>>> print(sum(nums))
15
#리스트에 저장된 개수 출력
>>> cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
>>> print(len(cook))
12
#리스트의 평균 출력
>>> nums = [1, 2, 3, 4, 5]
>>> print(sum(nums)/len(nums))
3.0
##or
>>> nums = [1, 2, 3, 4, 5]
>>> average = sum(nums) / len(nums)
>>> print(average)

#슬라이싱 활용
>>> price = ['20180728', 100, 130, 140, 150, 160, 170]
>>> print(price[1:])
[100, 130, 140, 150, 160, 170]
#슬라이싱 사용하여 홀수만 출력
>>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> print(nums[0::2])
[1, 3, 5, 7, 9]
#슬라이싱 사용하여 짝수만 출력
>>> print(nums[1::2])
[2, 4, 6, 8, 10]
#슬라이싱 사용하여 역 방향으로 출력
>>> nums = [1, 2, 3, 4, 5]
>>> print(nums[::-1])
[5, 4, 3, 2, 1]

>>> interest = ['삼성전자', 'LG전자', 'Naver']
>>> print(interest[::2])
['삼성전자', 'Naver']
#join 메서드
>>> interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
>>> '/'.join(interest)
'삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우'
>>> interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
>>> print("\n".join(interest))
삼성전자
LG전자
Naver
SK하이닉스
미래에셋대우
#문자열 split 메서드
>>> string = "삼성전자/LG전자/Naver"
>>> print(string.split("/"))
['삼성전자', 'LG전자', 'Naver']
#리스트 정렬
>>> data = [2, 4, 3, 1, 5, 10, 9]
>>> data.sort()
>>> data
[1, 2, 3, 4, 5, 9, 10]
>>> data = [2, 4, 3, 1, 5, 10, 9]
>>> data
[2, 4, 3, 1, 5, 10, 9]
>>> data = [2, 4, 3, 1, 5, 10, 9]
>>> data.sort()
>>> print(data)
[1, 2, 3, 4, 5, 9, 10]
>>> data = [2, 4, 3, 1, 5, 10, 9]
>>> data2=sorted(data)
>>> print(data2)
[1, 2, 3, 4, 5, 9, 10]



#튜플 생성
>>> my_variable=()
>>> my_variable
()
>>> print(type(my_variable))
<class 'tuple'>
>>> movie_rank=('닥터 스트레인지','스플릿','럭키')
>>> print(movie_rank)
('닥터 스트레인지', '스플릿', '럭키')
#숫자 1이 저장된 튜플 생성
>>> num=1,
>>> print(num)
(1,)
>>> 1
1
>>> type(1)
<class 'int'>
>>> a=1
>>> a=(1)
>>> type(a)
<class 'int'>
>>> a=(1,)
>>> type(a)
<class 'tuple'>
>>> t = 1, 2, 3, 4
>>> type(t)
<class 'tuple'>
>>> t = [1, 2, 3, 4]
>>> type(t)
<class 'list'>
>>> t = (1, 2, 3, 4)
>>> type(t)
<class 'tuple'>

>>> t = ('a', 'b', 'c')
>>> t[0]
'a'
>>> print(t[0])
a
>>> t = ('a', 'b', 'c')
>>> t[0] = 'A'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t = ('A', 'b', 'c')
>>> t
('A', 'b', 'c')
#튜플을 리스트로 변경
>>> interest = ('삼성전자', 'LG전자', 'SK Hynix')
>>> interest = ['삼성전자', 'LG전자', 'SK Hynix']
>>> print(interest)
['삼성전자', 'LG전자', 'SK Hynix']
#튜플을 리스트로 변경
>>> interest = ('삼성전자', 'LG전자', 'SK Hynix')
>>> data=list(interest)
>>> print(data)
['삼성전자', 'LG전자', 'SK Hynix']
#리스트를 튜플로 변경
>>> interest = ['삼성전자', 'LG전자', 'SK Hynix']
>>> data=(interest)
>>> print(data)
['삼성전자', 'LG전자', 'SK Hynix']
>>> data=tuple(interest)
>>> print(data)
('삼성전자', 'LG전자', 'SK Hynix')
#튜플 언팩킹
>>> temp = ('apple', 'banana', 'cake')
>>> a, b, c = temp
>>> print(a, b, c)
apple banana cake
#1~99까지의 정수 중 짝수만
>>> data = tuple(range(2, 100, 2))
print( data )
(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98)