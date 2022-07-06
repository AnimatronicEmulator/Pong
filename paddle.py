from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start_pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(255, 255, 255)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.speed("fastest")
        self.goto(start_pos)
        self.score = 0

    def north(self):
        self.setheading(90)
        self.forward(30)

    def south(self):
        self.setheading(270)
        self.forward(30)
