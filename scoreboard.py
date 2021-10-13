

from turtle import Turtle

class Score(Turtle):

    def __init__(self) :
        super().__init__()
        self.score=0
        self.color('white')
        self.penup()
        self.goto(0,260)
        self.updater()
        self.hideturtle()

    def updater(self):
        self.write(f"Score : {self.score} ",align='left',font=("arial", 20 , "normal"))
    
    def gameOver(self):
        self.goto(0,0)
        self.write(f"youre fuckin dead",align='left',font=("arial", 20 , "normal"))
    
    def incre(self):
        self.score+=1
        self.clear()
        self.updater()
