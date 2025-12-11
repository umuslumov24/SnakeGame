from turtle import Turtle
import os

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        if not os.path.exists("Highest_Score.txt"):
            with open("Highest_Score.txt", "w") as f:
                f.write("0")

        with open("Highest_Score.txt",'r') as theone:
            self.high_score = int(theone.read())

        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  High Score: {self.high_score}", align="center", font=('Courier', 15, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Highest_Score.txt","w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update()


    def increase(self):
        self.score+=1
        self.update()
