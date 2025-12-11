from turtle import Turtle

Move_step = 20
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.turtles = []
        self.create()
        self.head = self.turtles[0]

    def create(self):
        for position in starting_positions:
            self.add_news(position)

    def add_news(self, position):
        turtle = Turtle("square")
        turtle.penup()
        turtle.color("green")
        turtle.goto(position)
        self.turtles.append(turtle)

    def get_longer(self):
        self.add_news(self.turtles[-1].position())

    def move(self):
        for num in range(len(self.turtles)-1,0,-1):
            newx = self.turtles[num-1].xcor()
            newy = self.turtles[num-1].ycor()
            self.turtles[num].goto(newx, newy)
        self.head.forward(Move_step)

    def go_right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)

    def go_left(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)

    def go_up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)

    def go_down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)

    def collision(self):
        for segment in self.turtles[2:]:
            if self.head.distance(segment) <=2:
                return True
        return False


    def reset(self):
        for trek in self.turtles:
            trek.goto(650,650)
        self.turtles.clear()
        self.create()
        self.head = self.turtles[0]