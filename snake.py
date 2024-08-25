from turtle import Turtle

INITIAL_POSITION = [(0, 0), (20, 0), (40, 0)]
TURTLE_SHAPE = 'classic'
TURTLE_COLOR = 'white'
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
WALL_LEFT = -300
WALL_RIGHT = 300

class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for c in range(3):
            new_turtle = Turtle(shape=TURTLE_SHAPE)
            new_turtle.color(TURTLE_COLOR)
            new_turtle.penup()
            new_turtle.setposition(INITIAL_POSITION[c])
            self.turtles.append(new_turtle)

    def move(self):
        for turt in range(len(self.turtles) - 1, -1, -1):
            if turt > 0:
                self.turtles[turt].setposition(self.turtles[turt - 1].position())
                self.turtles[turt].setheading(self.turtles[turt - 1].heading())
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        new_turtle = Turtle(shape=TURTLE_SHAPE)
        new_turtle.speed('fastest')
        new_turtle.color(TURTLE_COLOR)
        new_turtle.penup()
        self.turtles.append(new_turtle)

    def hit_check(self):
        if self.head.xcor() >= WALL_RIGHT or self.head.xcor() <= WALL_LEFT \
            or \
            self.head.ycor() >= WALL_RIGHT or self.head.ycor() <= WALL_LEFT:
                return True

        for turtle in self.turtles[3:]:
            if self.head.distance(turtle) <= 10:
                return True

    def pos(self):
        return self.head.pos()

    def up_move(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down_move(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right_move(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left_move(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
