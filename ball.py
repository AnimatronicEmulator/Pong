from turtle import Turtle
import random
POSSIBLE_HEADINGS = [random.randint(-40, 40), random.randint(-140, 140)]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(255, 255, 255)
        self.shape("circle")
        self.speed("slow")
        self.reset_ball()

    def move(self):
        self.forward(1)

    def bounce(self, r_paddle, l_paddle):
        if self.ycor() > 290 or self.ycor() < -290:
            self.setheading(-self.heading())
        elif 340 < self.xcor() < 351 and self.distance(r_paddle) < 50:
            if int(self.distance(r_paddle)) == 0:
                self.setheading(180)
            else:
                angle = (89 / 50) * (self.ycor() - r_paddle.ycor()) + 90
                self.setheading(angle)
        elif -351 < self.xcor() < -340 and self.distance(l_paddle) < 50:
            if int(self.distance(l_paddle)) == 0:
                self.setheading(0)
            else:
                angle = (89 / 50) * (self.ycor() - l_paddle.ycor())
                self.setheading(angle)

    def reset_ball(self):
        self.goto(0, 0)
        self.setheading(random.choice(POSSIBLE_HEADINGS))
