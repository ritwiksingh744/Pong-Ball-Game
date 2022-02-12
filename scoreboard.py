from turtle import Turtle
FONT =("courier", 50, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-150, 200)
        self.write(f"A:{self.l_score}", align="center", font=FONT)
        self.goto(150, 200)
        self.write(f" B:{self.r_score}", align="center", font=FONT)

    def l_point(self):
        self.l_score +=1
        self.update_scoreboard()

    def r_point(self):
        self.r_score +=1
        self.update_scoreboard() 


    def game_over_A(self):
        self.color("red")
        self.goto(0, 0)
        self.write(f"Game Over\n A win", align="center",font=FONT) 

    def game_over_B(self):
        self.color("red")
        self.goto(0, 0)
        self.write(f"Game Over\n B win", align="center",font=FONT)               