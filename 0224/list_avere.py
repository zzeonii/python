#리스트의 평균 구하기

##1
def print_score(L):
    print(sum(L)/len(L))

##2
def print_score(L):
    _sum,_cnt=0,0
    for sco in L:
        _sum+=sco
        _cnt+=1
    print(_sum/_cnt)