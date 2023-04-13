from turtle import *
import time
color('red','yellow')
print(abs(pos()))
begin_fill()
while True:
    forward(200)
    time.sleep(1)  #딜레이 시간 주기
    left(160)
    time.sleep(1)
    print(abs(pos()))
    if abs(pos())<1:
        break
end_fill()