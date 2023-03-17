from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POINT = 0
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.xcor = STARTING_POINT
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]

    def make_snake(self):
        for i in range(0, 3):
            snake = Turtle("square")
            snake.color("white")
            snake.pu()
            snake.goto(x=self.xcor, y=0)
            self.xcor -= 20
            self.segments.append(snake)

    def add_body(self):
        new_body = Turtle("square")
        new_body.color("white")
        new_body.pu()
        new_x = self.segments[len(self.segments) - 1].xcor()
        new_y = self.segments[len(self.segments) - 1].ycor()
        new_body.speed("fastest")
        new_body.goto(new_x, new_y)
        self.segments.append(new_body)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(180)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(0)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.seth(90)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.seth(270)

    def move_snake(self):

        for num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[num - 1].xcor()
            new_y = self.segments[num - 1].ycor()
            self.segments[num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)
