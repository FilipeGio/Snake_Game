from turtle import Turtle

ALIGNING = 'center'


class Score:

    def __init__(self):
        self.board = Turtle()
        self.board.color('white')
        self.score = 0
        self.board.up()
        self.board.hideturtle()
        self.board.goto(0, 270)
        self.score_count()

    def score_count(self):
        self.board.clear()
        self.board.write(f'Score: {self.score}', align=ALIGNING, font=('Arial', 14, 'normal'))
        self.score += 1

    def game_over(self):
        self.board.goto(0, 0)
        self.board.write('GAME OVER', align=ALIGNING)
