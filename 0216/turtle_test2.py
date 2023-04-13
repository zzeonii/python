from turtle import *
color('blue','cyan')
begin_fill()
while True:
    print(abs(pos()))
    forward(200)
    left(170)
    if abs(pos())<1:
        break

end_fill()
# clear()
# bye()
