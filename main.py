from turtle import Screen
from paddle import Paddle
from display import Scoreboard, Divider, ScreenBorder
from ball import Ball


screen = Screen()
screen.setup(width=800, height=600)
screen.colormode(255)
screen.bgcolor(0, 0, 0)
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

scoreboard = Scoreboard()
divider = Divider()
ball = Ball()
borders = ScreenBorder()

screen.listen()
screen.onkey(key="w", fun=left_paddle.north)
screen.onkey(key="s", fun=left_paddle.south)
screen.onkey(key="Up", fun=right_paddle.north)
screen.onkey(key="Down", fun=right_paddle.south)

game_on = None
while game_on != 'yes':
    screen.update()

    ball.move()
    ball.bounce(right_paddle, left_paddle)

    # Calculate scoring
    if ball.xcor() > 390:
        left_paddle.score += 1
        ball.reset_ball()
        game_on = scoreboard.update_score(right_paddle.score, left_paddle.score)
    elif ball.xcor() < -390:
        right_paddle.score += 1
        ball.reset_ball()
        game_on = scoreboard.update_score(right_paddle.score, left_paddle.score)

screen.exitonclick()
