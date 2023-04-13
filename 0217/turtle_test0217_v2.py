from turtle import *
import time
color('blue','purple')
print(abs(pos()))
begin_fill()
while True:
    forward(200)
    time.sleep(1)
    left(170)
    time.sleep(1)
    print(abs(pos()))
    if abs(pos())<1:
        break
end_fill()
