#10가지 항목 
>>> for i in range(10):
    i
    
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

#0이상 10미만의 숫자 2칸씩 출력
>>> for i in range(0,10,2):
    i
    
0
2
4
6
8

#10이하 0초과의 숫자 -3칸씩 출력
>>> for i in range(10,0,-3):
    i
    
10
7
4
1
>>>

>>> range(1,6)
range(1, 6)
>>> list(range(1,6))
[1, 2, 3, 4, 5]
>>> *range(1,6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: MainCPythonBackend._install_repl_helper.<locals>._handle_repl_value() takes 1 positional argument but 5 were given

>>> [*range(1,6)] #풀기 연산자(unpacking operator)
[1, 2, 3, 4, 5]
>>> type(range(1,6))
<class 'range'>
>>> 