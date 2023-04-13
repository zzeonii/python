from turtle import *
color('blue','cyan')
abs(pos())
begin_fill()
while True:
    forward(200)
    left(170)
    abs(pos())
    if abs(pos())<1:
        break
end_fill()
# clear()
bye()
