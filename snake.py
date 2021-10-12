


from turtle import Screen, Turtle, tiltangle
from snakeMove import Snake
import time
from food import Food

s=Screen()
s.setup(height=700,width=700)
s.bgcolor('black')
s.title('sonake')
s.tracer(0)

totalTail=3

snake=Snake(totalTail)
food=Food()

s.listen()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.right,"Right")
s.onkey(snake.left,"Left")


gamOn=True

while gamOn:
    s.update()
    # snake.randomFood()
    time.sleep(.089)
    snake.move()

    if snake.head.distance(food)<15:
        food.newLoc()
        totalTail+=1
        snake.newHead( totalTail)




s.exitonclick()