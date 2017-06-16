import turtle

def draw_square(beluga):

    for count in range(0,4):
        beluga.forward(100)
        beluga.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("grey")
    beluga = turtle.Turtle()
    beluga.shape("turtle")
    beluga.color("blue")
    beluga.speed(5)
    # for i in range(1,7):
    #
    #     beluga.circle(100)
    #     beluga.right(10)
        # beluga.circle(100)
    # window.exitonclick()
    # for i in range (0, 5):
    #     draw_square(beluga)
    #     # beluga.right(i*30)
    #     beluga.setheading(i*30)



    for i in range (0, 27):
        beluga.color("#4477bb")
        beluga.forward(120)
        beluga.left(90)
        beluga.forward(50)
        beluga.left(90)
        beluga.forward(130)
        beluga.left(90)
        beluga.forward(120)

        beluga.right(100)


    window.exitonclick()


draw_art()
# draw_square()
# draw_circle()
# draw_triangle()
