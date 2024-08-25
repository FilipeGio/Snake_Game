from turtle import Turtle
from random import choice

FOOD_SHAPE = 'circle'


class Food:

    def __init__(self):
        self.turtle_food = Turtle(shape=FOOD_SHAPE)
        self.turtle_food.resizemode('user')
        self.turtle_food.shapesize(stretch_wid=0.4)
        self.turtle_food.color('white')
        self.turtle_food.penup()
        self.refresh()

    def refresh(self):
        num_list = []
        for c in range(-280, 300, 20):
            num_list.append(c)

        food_position = (choice(num_list), choice(num_list))
        self.turtle_food.setposition(food_position)









