import turtle
class Scorecard:
    def __init__(self):
        self.t1 = turtle.Turtle()
        self.t1.hideturtle()
        self.t1.color('white')
        self.t1.penup()
        self.t1.goto(0,-400)
        self.partition()
        self.t2 = turtle.Turtle()
        self.t2.penup()
        self.t2.hideturtle()
        self.t2.color('white')
        self.t2.goto(-200,350)
        self.t3 = turtle.Turtle()
        self.t3.penup()
        self.t3.hideturtle()
        self.t3.color('white')
        self.t3.goto(200,350)
    def partition(self):
        while(self.t1.ycor()!=400):
            self.t1.goto(0,self.t1.ycor()+10)
            if(self.t1.isdown()):
                self.t1.penup()
            else:
                self.t1.pendown()

    def display1(self,score3):
        self.t2.clear()
        
        self.t2.write(f'{score3}',font=("Arial",20,'italic'))
        
    def display2(self,score4):
        self.t3.clear()
        self.t3.write(f'{score4}',font=("Arial",20,'italic'))