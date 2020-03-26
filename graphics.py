import turtle

unit_length = 20


def diagonal():
    return (2*unit_length**2)**(1/2)*0.2


pen: turtle.Turtle = None
screen = None
x_current = 0
y_current = 0
width = None
height = None


def initialize(_width, _height):
    # module parameter setup
    global width, height
    global pen, screen
    pen = turtle.Turtle()
    pen._tracer(0, 0)  # Instant drawing
    pen.hideturtle()
    screen = turtle.Screen()
    width = _width
    height = _height
    # turtle setup
    screen.setup((width + 2) * unit_length, (height + 2) * unit_length)
    move_top()


def move_top():
    global x_current, y_current
    pen.goto(0, 0)
    pen.penup()
    pen.setheading(180)
    pen.forward(width * unit_length / 2)
    pen.setheading(90)
    pen.forward(height * unit_length / 2)
    pen.setheading(0)
    y_current = 0
    x_current = 0


# WALLS
def n_wall():
    pen.pendown()
    pen.forward(unit_length)
    pen.penup()
    pen.backward(unit_length)


def e_wall():
    dim = unit_length
    pen.forward(dim)
    pen.pendown()
    pen.setheading(-90)
    pen.forward(dim)
    pen.penup()
    pen.backward(dim)
    pen.setheading(0)
    pen.backward(dim)


def s_wall():
    pen.setheading(-90)
    pen.forward(unit_length)
    pen.pendown()
    pen.setheading(0)
    pen.forward(unit_length)
    pen.penup()
    pen.backward(unit_length)
    pen.setheading(90)
    pen.forward(unit_length)
    pen.setheading(0)


def w_wall():
    pen.setheading(-90)
    pen.pendown()
    pen.forward(unit_length)
    pen.penup()
    pen.backward(unit_length)
    pen.setheading(0)


def goal():
    pen.pendown()
    pen.fillcolor('red')
    pen.begin_fill()
    pen.forward(unit_length)
    pen.setheading(-90)
    pen.forward(unit_length)
    pen.setheading(180)
    pen.forward(unit_length)
    pen.setheading(90)
    pen.forward(unit_length)
    pen.end_fill()
    pen.penup()
    pen.setheading(0)


def u_arrow():
    pen.setheading(-90)  # go bottom-middle
    pen.forward(unit_length)
    pen.setheading(0)
    pen.forward(unit_length/2)
    pen.setheading(90)
    arrow()  # draw arrow
    pen.setheading(180)  # return top-left
    pen.forward(unit_length/2)
    pen.setheading(90)
    pen.forward(unit_length)
    pen.setheading(0)


def r_arrow():
    pen.setheading(-90)  # go left-middle
    pen.forward(unit_length/2)
    pen.setheading(0)
    arrow()  # draw arrow
    pen.setheading(90)  # return top-left
    pen.forward(unit_length/2)
    pen.setheading(0)


def d_arrow():
    pen.forward(unit_length/2)  # go top-middle
    pen.setheading(-90)
    arrow()  # draw arrow
    pen.setheading(0)
    pen.backward(unit_length/2)


def l_arrow():
    pen.forward(unit_length)
    pen.setheading(-90)
    pen.forward(unit_length/2)
    pen.setheading(180)
    arrow()
    pen.setheading(90)
    pen.forward(unit_length/2)
    pen.setheading(180)
    pen.forward(unit_length)
    pen.setheading(0)


def arrow():
    space = int(unit_length*0.2)
    arrow_len = unit_length-2*space
    d = diagonal()
    pen.forward(space)
    pen.pendown()
    pen.forward(arrow_len)
    pen.left(135)
    pen.forward(d)
    pen.backward(d)
    pen.left(90)
    pen.forward(d)
    pen.penup()
    pen.backward(d)
    pen.left(135)
    pen.backward(arrow_len+space)


# Move to the next cell
def _next():
    global x_current, y_current
    global width, height
    pen.penup()
    pen.setheading(0)
    newline = next_coordinates()
    if newline is False:
        pen.forward(unit_length)
    elif newline is True:
        pen.backward((width - 1) * unit_length)
        pen.setheading(-90)
        pen.forward(unit_length)
        pen.setheading(0)


def next_coordinates():
    global x_current, y_current
    y_current += 1
    if y_current >= width:
        y_current = 0
        x_current += 1
        if x_current >= height:
            return None
        else:
            return True
    return False


def draw_action(action):
    if 0 not in action:
        n_wall()
    if 1 not in action:
        e_wall()
    if 2 not in action:
        s_wall()
    if 3 not in action:
        w_wall()
    if 4 in action:
        goal()
    _next()


def draw_move(move):
    if move == 0:
        u_arrow()
    elif move == 1:
        r_arrow()
    elif move == 2:
        d_arrow()
    elif move == 3:
        l_arrow()
    _next()


def draw(env, policy):
    width = env.y()
    height = env.x()
    actions = env.actions.flatten()
    initialize(width, height)
    pen.color('blue')
    for action in actions:
        draw_action(action)
    move_top()
    pen.color('gray')
    for move in policy.flatten():
        draw_move(move)
    pen._update()  # Activate the screen (for instant drawing)
    turtle.done()


# Example
if __name__ == '__main__':
    acts = [{2, 3} for x in range(30)]
    draw(10, 3, acts, [])
