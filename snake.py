from turtle import Turtle

# Constants
INIT_POSITIONS = [(0, 0), (-11, 0), (-22, 0)]
MOVE_DISTANCE = 10

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.set_position()
        self.snake_head = self.segments[0]

    def set_position(self):
        """Initialises the position of a snake turtle"""
        for position in INIT_POSITIONS:
            # invoke the design_snake() and pass it an init_pos for each snake
            self.design_snake(position)

    def design_snake(self, position):
        """Creates the default appearance and position of a snake instance"""
        snake_segment = Turtle("square")
        snake_segment.color("white")
        snake_segment.shapesize(stretch_wid=.5, stretch_len=.5)
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend(self):
        """Add new segment to the snake"""
        self.design_snake(self.segments[-1].position())

    def move(self):
        """Moves the snake automatically"""
        for seg_num in range(len(self.segments) - 1, 0, -1):

            # get the x and y co-ordinates of the second last snake_segments
            # set the x and y co-ordinates of last snake_segment to the new
            # x and y values...
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # move the first snake_segment to a new x & y position
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        """Sets the heading of the first snake_segment 90 degrees north"""
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        """Sets the heading of the first snake_segment 270 degrees south"""
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        """Sets the heading of the first snake_segment 180 degrees west"""
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        """Sets the heading of the first snake_segment 0 degrees east"""
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
