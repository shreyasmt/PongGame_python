import turtle
import winsound
#create a window

wn = turtle.Screen()
wn.title("PY by Shreya")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)            #Stops the window updating speeds up the game

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #to set the spped this sets a maximum possible speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0) #to set the spped this sets a maximum possible speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0) #to set the spped this sets a maximum possible speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
#seperating the movement in to 2 parts
ball.dx = 0.1
ball.dy = -0.1                             # the ball moves every 2 pixels since x is positive it moves right and y moves up


#pen 

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#Score

score_a = 0
score_b = 0



#Function
def paddle_a_up():
    y=paddle_a.ycor() #returns the y coordinate
    y +=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor() #returns the y coordinate
    y -=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor() #returns the y coordinate
    y +=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor() #returns the y coordinate
    y -=20
    paddle_b.sety(y)

# keyboard binding

wn.listen() #listen for keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
#main loog of the game

while True:
    wn.update()
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  
    # paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350)  and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if (ball.xcor() < -340 and ball.xcor() > -350)  and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)