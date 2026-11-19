import turtle
import random

def ret_random_pos():
    screen_width = screen.window_width()
    screen_height = screen.window_height()
    rand_x = random.randint(int(screen_width / 2) * -1, int(screen_width / 2) )
    rand_y = random.randint(int(screen_height / 2) * -1, int(screen_height / 2) )
    print(f"random {rand_x} {rand_y}")
    return rand_x, rand_y

def one_square():
    color1 = random.choice(colors)
    color2 = random.choice(colors)
    length = 100
    pen.color(color1)
    pen.pensize(30)
    pen.shape("turtle")
    pen.fillcolor(color2)
    pen.begin_fill()

    canvas = screen.getcanvas()
    pointer_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    pointer_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    x = canvas.canvasx(pointer_x)
    y = -canvas.canvasy(pointer_y)

    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    for side in range(4):
        pen.forward(length)
        pen.right(90)
    pen.end_fill()

def draw_many_squares(pen):
    for i in range(10):
        outer_color = random.choice(colors)
        inner_color = random.choice(colors)
        pen.penup()
        rand_x, rand_y = ret_random_pos()
        pen.goto(rand_x, rand_y)
        pen.pendown()
        one_square()
        pen.penup()

def draw_flower(x,y):
    pen.penup()
    pen.pensize(1)
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor(random.choice(colors))
    pen.begin_fill()

    for petal in range(8):
        pen.circle(30)
        pen.right(45)

    pen.end_fill()
    pen.penup()

def draw_flower_big(x=None,y=None):
    if x is None or y is None:
        x, y = ret_random_pos()
    pen.penup()
    pen.pensize(1)
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor(random.choice(colors))
    pen.begin_fill()

    for petal in range(8):
        pen.circle(50)
        pen.right(45)

    pen.end_fill()
    pen.penup()
    pen.penup()

# rand_x, rand_y = ret_random_pos()

    pen.pensize(1)
    pen.goto(x,y)
    pen.pendown()
    pen.fillcolor(random.choice(colors))
    pen.begin_fill()

    for petal in range(8):
        pen.circle(30)
        pen.right(45)

    pen.end_fill()
    pen.penup()

def draw_many_flowers(pen):
    pen.pensize(4)
    for i in range(40):
        draw_flower(*ret_random_pos())

def draw_many_flowers_big(pen):
    pen.pensize(10)
    for i in range(20):
        draw_flower_big(*ret_random_pos())

def bg_cl():
    screen.bgcolor("blue")

colors = [
    "hot pink",
    "coral",
    "tomato",
    "orange",
    "gold",
    "yellow",
    "orchid",
    "violet",
    "purple",
    "magenta",
    "deep pink",
    "turquoise",
    "medium aquamarine",
    "sky blue",
    "plum",
    "salmon",
    "light pink",
    "medium violet red",
    "spring green",
    "khaki"
]

screen = turtle.Screen()
screen.title("My Screen")
screen.bgcolor("hot pink")
pen = turtle.Turtle()
pen.speed(0)
pen.penup()

def main():
    global screen
    global pen
    screen = turtle.Screen()
    screen.title("MY Screen")
    screen.bgcolor("hot pink")

    pen = turtle.Turtle()
    pen.speed(0)

    screen.listen()
    screen.onclick(draw_flower)
    screen.onkey(one_square, "a")
    screen.onkey(bg_cl, "r")
    screen.onkey(draw_flower_big,"i")

    canvas = screen.getcanvas()
    canvas.bind("<Motion>",one_square)


    turtle.done()


if __name__ == "__main__":
    main()

# TODO: Register draw_flower as the mouse-click handler.
# TODO: Register one_square with the "a" key.
# TODO: Enable keyboard listening.

'''
I chose the interactive garden. I added the keyboard command "r" that changes the background color to blue. I also added that when "i" is pressed the turtle draws a larger flower in a random posistion.
'''