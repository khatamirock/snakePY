


from turtle import Screen, Turtle, distance, tiltangle
from snakeMove import Snake
from scoreboard import Score
import time
from food import Food

s=Screen()
handW=600

s.setup(height=handW,width=handW)
s.bgcolor('black')
s.title('sonake')
s.tracer(0)

totalTail=3

snake=Snake(totalTail)
food=Food()
score=Score()

s.listen()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.right,"Right")
s.onkey(snake.left,"Left")


gamOn=True
deadLim=(handW//2)-5
while gamOn:


    if snake.head.xcor() >deadLim or snake.head.xcor() <-deadLim or snake.head.ycor() >deadLim or snake.head.ycor() <-deadLim :
        score.gameOver()
        gamOn=False
    s.update()
    time.sleep(.089)
    snake.move()

    if snake.head.distance(food)<15:
        food.newLoc()
        totalTail+=1
        snake.newHead( totalTail)
        score.incre()
    for seg in snake.snls:
        if seg==snake.head:
            pass
        elif snake.head.distance(seg)<10:
            score.gameOver()
            gamOn=False
            
    



s.exitonclick()