from turtle import Screen
from Snakes import Snake
import time
from Food import Food
from SB import Scoreboard

ekran = Screen()
ekran.setup(600, 600)
ekran.bgcolor('black')
ekran.title("Traditional Snake Game")
ekran.tracer(0)

turtle = Snake()
f = Food()
myboard = Scoreboard()

ekran.listen()
ekran.onkey(key="Up",fun= turtle.go_up)
ekran.onkey(key="Down",fun= turtle.go_down)
ekran.onkey(key="Left",fun= turtle.go_left)
ekran.onkey(key="Right",fun= turtle.go_right)

is_on = True

while is_on:
    ekran.update()
    time.sleep(0.1)
    turtle.move()

    if turtle.head.distance(f) < 15:
        f.recreation()
        myboard.increase()
        turtle.get_longer()

    if turtle.head.xcor() > 295 or turtle.head.xcor() < -295 or turtle.head.ycor() > 295 or turtle.head.ycor() < -295:
        myboard.reset()
        turtle.reset()

    if turtle.collision():
        myboard.reset()
        turtle.reset()

ekran.exitonclick()