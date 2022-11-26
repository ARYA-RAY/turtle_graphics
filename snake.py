from turtle import  Turtle

pos_list = [(0,0),(-20,0),(-40,0)]
dist_move = 20
up = 90
left = 180
down = 270
right = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in pos_list:
            self.add_segment(i)

    def add_segment(self,i):
        new_part = Turtle("circle")
        new_part.color("green")
        new_part.penup()
        new_part.goto(i)
        self.segments.append(new_part)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(dist_move)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
