#if / if-else / if-elif-else
#만약 나이가 19살 이상이면 성인입니다
age=25
if age>=19:
    '성인'


#만약 나이가 19살 이상이면 성인이고 아니면 미성년자 입니다
age=17
if age>=19:
    '성인'
else :
    '미성년자'

#만약 태어난 해가 1981~1996년 사이면 M세대, 1997~2012년 사이이면 Z세대, 그 이후는 애기야
birth_year=2002
if 1981<= birth_year<=1996:
    'M세대'
elif 1997<= birth_year<=2012:
    'Z세대'
else :
    '애기'
