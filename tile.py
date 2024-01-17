import turtle
POS = [0,20,40]
DIS = 40
class Tiles:
    def __init__(self,side):
        self.parts1 = []
        self.creator(side)
    def creator(self,side):
        for i in range(3):
            t1 = turtle.Turtle(shape='square')
            t1.speed("fastest")
            t1.color('white')
            t1.penup()
            t1.goto(side,POS[i])
            t1.setheading(90)
            self.parts1.append(t1)
    def mvup(self):
        if(self.parts1[2].ycor()>=390):
            pass
        else:
            for i in range(3):
                self.parts1[i].goto(self.parts1[i].xcor(),self.parts1[i].ycor()+DIS)
    
    def mvdown(self):
        if(self.parts1[0].ycor()<=-390):
            pass
        else:
            for i in range(3):
                self.parts1[i].goto(self.parts1[i].xcor(),self.parts1[i].ycor()-DIS)
    
        