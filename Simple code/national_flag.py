from turtle import *
speed(5)
goto(-300,0)
color('green')
begin_fill()
for i in range(4):
    forward(600-(i%2)*300)
    left(90)
end_fill()
goto(0,30)
begin_fill()
color('red')
circle(120)
end_fill()
penup()
goto(-300,300)
begin_fill()
for i in range(4):
    color('black')
    right(90)
    forward(900-(i%2)*880)
end_fill()
done()
    
   



