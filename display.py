from turtle import Turtle
FONT = ("Courier", 50, "bold")
ALIGNMENT = "center"
CENTER_LINES_NUM = 20
BORDER_POSITIONS = [(0, 300), (0, -300), (-400, 0), (400, 0)]


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(255, 255, 255)
        self.hideturtle()
        self.penup()
        self.goto(0, 220)
        self.update_score(0, 0)

    def update_score(self, r_paddle_score, l_paddle_score):
        self.clear()
        self.write(f"{l_paddle_score}  {r_paddle_score}", font=FONT, align=ALIGNMENT)
        if r_paddle_score == 10:
            self.end_game_message("right", r_paddle_score, l_paddle_score)
            return 'yes'
        elif l_paddle_score == 10:
            self.end_game_message("left", l_paddle_score, r_paddle_score, )
            return 'yes'

    def end_game_message(self, winning_player, winning_score, other_score):
        self.color(255, 255, 255)
        if winning_player == "left":
            self.goto(-200, 0)
            self.write(f"You won!\nFinal scores: {winning_score} to {other_score}",
                       align="center",
                       font=("Courier", 20, "bold"))
        elif winning_player == "right":
            self.goto(200, 0)
            self.write("something else")


class Divider:
    def __init__(self):
        self.lines = []
        self.line_maker()

    def line_maker(self):
        gap = 10
        line_y_coord = -285
        for x in range(CENTER_LINES_NUM):
            new_line = Turtle("square")
            new_line.penup()
            new_line.color(255, 255, 255)
            new_line.shapesize(stretch_len=0.2, stretch_wid=0.75)
            new_line.goto(0, line_y_coord)
            new_line.speed("fastest")
            line_y_coord += (20 + gap)
            self.lines.append(new_line)


class ScreenBorder:
    def __init__(self):
        self.borders = []
        self.border_generator()

    def border_generator(self):
        for position in BORDER_POSITIONS:
            new_border = Turtle("square")
            new_border.penup()
            new_border.color(255, 255, 255)
            new_border.goto(position)
            new_border.setheading(90)
            if position[0] != 0:
                new_border.shapesize(stretch_wid=0.1, stretch_len=30)
                new_border.setheading(90)
            elif position[1] != 0:
                new_border.shapesize(stretch_wid=40, stretch_len=0.1)
            self.borders.append(new_border)
