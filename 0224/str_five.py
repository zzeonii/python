#입력 문자열을 한 줄에 다섯글자씩 출력

##1
def print_5xn(string):
    _cnt=0
    for s in string:
        print(s,end='')
        _cnt+=1
        if _cnt%5==0:
            print()
##2            
def print_5xn(string):
    for _cnt,s in enumerate(string):
        print(s,end='')
        if _cnt%5==4:
            print()
            
##예제의 답안
def print_5xn(line):
    chunk_num = int(len(line) / 5)
    for x in range(chunk_num + 1) :
        print(line[x * 5: x * 5 + 5])            

            
>>> print_5xn("아이엠어보이유알어걸")
아이엠어보
이유알어걸
>>> 