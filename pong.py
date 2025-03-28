import turtle
import time
##############################################
win = turtle.Screen()
win.title("Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)
##############################################
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.goto(-390, 290)
border.pendown()
border.pensize(3)
for _ in range(2):
    border.forward(780)
    border.right(90)
    border.forward(580)
    border.right(90)
border.hideturtle()
##############################################
cline = turtle.Turtle()
cline.color("white")
cline.goto(0, 300)
cline.setheading(270)
cline.pensize(2)
cline.hideturtle()
for _ in range(30):
    cline.penup()
    cline.forward(10)
    cline.pendown()
    cline.forward(10)
##############################################
a = 0
b = 0
x = turtle.Turtle()
x.speed(0)
x.shape("square")
x.color("lightblue")
x.shapesize(stretch_wid=6, stretch_len=1)
x.penup()
x.goto(-350, 0)
##############################################
y = turtle.Turtle()
y.speed(0)
y.shape("square")
y.color("lightcoral")
y.shapesize(stretch_wid=6, stretch_len=1)
y.penup()
y.goto(350, 0)
##############################################
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2
##############################################
disp = turtle.Turtle()
disp.speed(0)
disp.color("white")
disp.penup()
disp.hideturtle()
disp.goto(0, 260)
disp.write("Player A: 0    Player B: 0", align="center", font=("Courier", 24, "bold"))
##############################################
def up_1():
    y = x.ycor()
    y += 50
    if y > 240:
        y = 240
    x.sety(y)
##############################################
def down_1():
    y = x.ycor()
    y -= 50
    if y < -240:
        y = -240
    x.sety(y)
##############################################
def up_2():
    y_pos = y.ycor()
    y_pos += 50
    if y_pos > 240:
        y_pos = 240
    y.sety(y_pos)
##############################################
def down_2():
    y_pos = y.ycor()
    y_pos -= 50
    if y_pos < -240:
        y_pos = -240
    y.sety(y_pos)
##############################################
win.listen()
win.onkeypress(up_1, "w")
win.onkeypress(down_1, "s")
win.onkeypress(up_2, "Up")
win.onkeypress(down_2, "Down")
##############################################
def start():
    countdown = turtle.Turtle()
    countdown.color("white")
    countdown.hideturtle()
    countdown.penup()
    for i in range(3, 0, -1):
        countdown.goto(0, 0)
        countdown.write(f"Starting in {i}", align="center", font=("Courier", 48, "bold"))
        win.update()
        time.sleep(1)
        countdown.clear()
    countdown.goto(0, 0)
    countdown.write("Go!", align="center", font=("Courier", 48, "bold"))
    win.update()
    time.sleep(1)
    countdown.clear()
##############################################
start()
##############################################
def end(winner):
    disp.clear()
    disp.goto(0, 0)
    disp.write(f"{winner} Wins!", align="center", font=("Courier", 36, "bold"))
    disp.goto(0, -50)
    disp.write("Press 'r' to Restart", align="center", font=("Courier", 24, "normal"))
##############################################
def reset():
    global a, b
    a = 0
    b = 0
    ball.goto(0, 0)
    ball.showturtle()
    ball.dx = 0
    ball.dy = 0
    x.goto(-350, 0)
    x.showturtle()
    y.goto(350, 0)
    y.showturtle()
    disp.clear()
    disp.goto(0, 260)
    disp.write(f"Player A: {a}    Player B: {b}", align="center", font=("Courier", 24, "bold"))
    main()
##############################################
win.onkeypress(reset, "r")
##############################################
def main():
    global a, b
    while True:
        win.update()
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        if ball.ycor() > 280:
            ball.sety(280)
            ball.dy *= -1
        if ball.ycor() < -280:
            ball.sety(-280)
            ball.dy *= -1
        if ball.xcor() > 370:
            a += 1
            disp.clear()
            disp.write(f"Player A: {a}    Player B: {b}", align="center", font=("Courier", 24, "bold"))
            ball.goto(0, 0)
            ball.dx = -ball.dx
            time.sleep(1)
        if ball.xcor() < -370:
            b += 1
            disp.clear()
            disp.write(f"Player A: {a}    Player B: {b}", align="center", font=("Courier", 24, "bold"))
            ball.goto(0, 0)
            ball.dx = -ball.dx
            time.sleep(1)
        if (340 < ball.xcor() < 350) and (y.ycor() - 60 < ball.ycor() < y.ycor() + 60):
            ball.setx(340)
            ball.dx = -ball.dx
        if (-350 < ball.xcor() < -340) and (x.ycor() - 60 < ball.ycor() < x.ycor() + 60):
            ball.setx(-340)
            ball.dx = -ball.dx
        if a >= 10 or b >= 10:
            winner = "Player A" if a > b else "Player B"
            ball.hideturtle()
            x.hideturtle()
            y.hideturtle()
            end(winner)
            break
##############################################
main()
win.mainloop()
##############################################
