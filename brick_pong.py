from turtle import *

player_score = 0
player_max_score = 0

# Creating screen
court = Screen()
court.title("LogPong v 0.3")
court.setup(width=800, height=600)
court.bgcolor('black')
court.tracer(0)

# Creating ball
ball = Turtle()
ball.shape("circle")
ball.color("green")
ball.penup()
ball.setpos(0, 0)

# Creating ball movement speed
def init():
    global ball, want_continue
    ball.step_x = 0.5
    ball.step_y = 0.5
    ball.setpos(0, 0)
    want_continue = True


def on_quit():
    global want_continue
    want_continue = False


court.onkey(on_quit, "q")
court.listen()

# Creating point screen
point = Turtle()
point.speed(0)
point.color('red')
point.penup()
point.hideturtle()
point.goto(0,260)
point.write("Player: 0 ",align="center",font=('Monaco',24,"bold"))

#Creating maximum point screen
pointmax = Turtle()
pointmax.speed(0)
pointmax.color('red')
pointmax.penup()
pointmax.hideturtle()
pointmax.goto(-350,260)
pointmax.write("Max:0",align="center",font=('Monaco',24,"bold"))

# Creating racket
racket = Turtle()
racket.hideturtle()
racket.shape("square")
racket.color("white")
racket.penup()
racket.goto(0, -285)
racket.shapesize(1, 3)
racket.showturtle()

# Creating arrows to move the racket
def racket_left():
    x =racket.xcor()
    x = x - 15
    racket.setx(x)


def racket_right():
    x = racket.xcor()
    x = x + 15
    racket.setx(x)

court.listen()

court.onkeypress(racket_left, "Left")
court.onkeypress(racket_right, "Right")


# Creating borders to the ball
def move_ball():
    global ball
    global player_score
    global player_max_score

    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.step_x *= -1

    if ball.ycor() > 290:
        ball.step_y *= -1

    if ball.ycor() < -290:
        ball.setpos(0, 0)
        ball.step_y *= -1
        player_score= 0
        point.clear()
        point.write("Player: {} ".format(player_score), align="center", font=('Monaco', 24, "bold"))



    ball.setx(ball.xcor() + ball.step_x)
    ball.sety(ball.ycor() + ball.step_y)

#Racket ball border
    if (ball.ycor() < - 265) and ball.ycor() > - 275 \
            and (racket.xcor() + 32 > ball.xcor() > racket.xcor() - 32) :
        ball.sety(-265)
        ball.step_y = ball.step_y * -1
        player_score += 1
        point.clear()
        point.write("Player: {}".format(player_score),align="center",font=('Monaco',24,"bold"))
#Racker border
    if racket.xcor() < -400:
        racket.setx(400)

    if racket.xcor() >400:
        racket.setx(-400)


#Maximum point show
    if player_score > player_max_score:
        player_max_score = player_score
        pointmax.clear()
        pointmax.write("Max:{}".format(player_max_score),align="center",font=('Monaco',24,"bold"))


def run():
    global ball, want_continue
    while want_continue:
        move_ball()
        court.update()





#
init()
run()

court.bye()
