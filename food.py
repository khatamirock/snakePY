from turtle import Turtle, setworldcoordinates
import random
class Food(Turtle):

    def __init__(self):
        super().__init__() 
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.shapesize(0.5,0.5)

        self.newLoc()
        
    def newLoc(self):
        rax=random.randint(-280,290)
        ray=random.randint(-290,290)
        self.goto(rax,ray)
    