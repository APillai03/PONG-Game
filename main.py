from turtle import Screen
from tile import Tiles
from ball import Ball
from score import Scorecard
import time

GAME = True

root = Screen()
root.title('PONG')
root.setup(height=800,width=800)
root.bgcolor('black')
root.tracer(0)
root.listen()

def stop_movement():
    root.onkey(None, 'Up')

def pause():
    GAME = False
tile1 = Tiles(-390)
tile2 = Tiles(380)
ball = Ball()
root.onkeypress(tile1.mvup,'w')
root.onkeypress(tile1.mvdown,'s')

root.onkeypress(tile2.mvup,'Up')
root.onkeypress(tile2.mvdown,'Down')

root.onkeyrelease(stop_movement,'Up')

root.onkey(pause,'p')


score1 = 0
score2 = 0

score = Scorecard()
while GAME:
    time.sleep(0.07)
    root.update()
    ball.move()
    if(ball.ycor()>380) or (ball.ycor()<-380) :
        ball.colly()
    if(ball.distance(tile1.parts1[0])<20) or (ball.distance(tile1.parts1[1])<20) or (ball.distance(tile1.parts1[2])<20):
        ball.collx()
    if(ball.distance(tile2.parts1[0])<20) or (ball.distance(tile2.parts1[1])<20) or (ball.distance(tile2.parts1[2])<20):
        ball.collx()
    if(ball.xcor()>400):
        score2+=1
        ball.reset()
    elif(ball.xcor()<-400):
        score1+=1
        ball.reset()
    score.display1(score3=score2)
    score.display2(score4=score1)

















root.exitonclick()