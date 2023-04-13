#예제 답안
def print_max(a, b, c) :
    max_val = 0
    if a > max_val :
        max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c
    print(max_val)

#1
def print_max(a,b,c):
    if a>=b:
        if a>=c:
            print(a)
        else:
            print(c)
    else:
        if b>=c:
            print(b)
            
#2
def print_max(a,b,c):
    if a>=b and a>=c:
        print(a)
    elif a>=b and a<c:
        print(c)
    elif a<b and b>=c:
        print(b)
        
#3
def print_max(a,b,c):
    _max=a
    if b>_max:
        _max=b
    if c>_max:
        _max=c
    print(_max)
    
#4
def print_max(a,b,c):
    _max=a
    L=[b,c]
    for i in L:
        if i>_max:
            _max=i
    print(_max)