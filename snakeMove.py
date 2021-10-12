
from turtle import Turtle, done
# snls=[]
item=5
UP=90
DOWN=270
RIGHT=0
LEFT=180

from random import randint as rint
class Snake:
    def __init__(self,it) -> None:
        self.snls=[]
        self.ls=[-20*x for x in range(it)]
        self.crate()
        # self.ls.reverse()
        self.head=self.snls[0]
    
    def crate(self):
        for x in self.ls:
            tim = Turtle('square')
            tim.color('white')
            tim.penup()
            tim.goto(x,0)

            self.snls.append(tim)

    
    def move(self):
        for xs in range(len(self.snls)-1,0,-1):
            xc=self.snls[xs-1].xcor()
            yc=self.snls[xs-1].ycor()
            self.snls[xs].goto(xc,yc)
            # xs.forward(20)
        # for xs in range(len(self.snls)-1):
        #     xc=self.snls[xs+1].xcor()
        #     yc=self.snls[xs+1].ycor()
        #     self.snls[xs].goto(xc,yc)

        self.head.forward(20)
        self.head.color('red')
      
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    
    def randomFood(self):
        randx=rint(0,700)
        randy=rint(0,700)
        tim = Turtle('square')
        tim.color('white')
        tim.penup()
        tim.goto(randx,randy)
    
    def newHead(self,t):
        
        tim = Turtle('square')
        tim.color('white')
        tim.penup()
        tim.speed('fastest')
        # tim.goto(self.snls[len(self.snls)-1],0)
        # lstPos=self.snls[t-1]
        t-=1
        xc=self.snls[-1].xcor()
        yc=self.snls[-1].ycor()
        tim.goto(xc,yc)
        self.snls.append(tim)

        # self.snls.append(t)