from turtle import *
color('red','yellow')
while True:
    print(abs(pos()))
    forward(200)
    left(170)
    if abs(pos())<1:
        break

end_fill()
clear()
bye()
