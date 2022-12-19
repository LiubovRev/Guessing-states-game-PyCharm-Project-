from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.update_score(

    def increase_score(self):
        self.score += 1
        self.clear()

