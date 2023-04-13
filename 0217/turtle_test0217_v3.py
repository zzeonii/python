from turtle import *
import time
color('black','red')
print(abs(pos()))
begin_fill()
while True:
    forward(200)
    time.sleep(1)
    left(160)
    time.sleep(1)
    print(abs(pos()))
    if abs(pos())<1:
        break
end_fill()