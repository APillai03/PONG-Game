from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.speed('normal')
        self.goto(-100,0)
        self.xm = 13
        self.ym = 13

    def move(self):
        nx = self.xcor() + self.xm
        ny = self.ycor() + self.ym
        self.goto(nx,ny)

    def colly(self):
        self.ym *=-1

    def collx(self):
        self.xm *=-1

    def reset(self):
        self.goto(-70,0)
