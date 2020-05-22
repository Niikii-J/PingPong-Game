# This is my first non-text based game in Python!

import turtle
import winsound
import pygame
from pygame import mixer

wn = turtle.Screen()
wn.title("Pong by @Nicky.J")
wn.bgcolor("purple")
wn.bgpic("purple.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

#BG music:
pygame.init()
mixer.music.load('melodyloops-the-first-light.wav')
mixer.music.play(-1)

# Score:
score_a = 0
score_b = 0

# Paddle A:
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B:
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball:
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.4
ball.dy = 0.4

# Pen score:
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  ||  Player B: 0", align="center", font=("Courier", 22, "normal"))

# Instructions for playing:
direction = turtle.Turtle()
direction.color("white")
direction.penup()
direction.hideturtle()
direction.goto(0, -260)
direction.write("Press w and s to move Player A. Press up and down to move Player B.", align="center", font=("Courier", 12, "normal"))

# Functions:
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard Binding:
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main game loop:

while True:
    wn.update()

    # Move the ball:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking:
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("boop.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("boop.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  ||  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 22, "normal"))
        winsound.PlaySound("ice_cubes.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  ||  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 22, "normal"))
        winsound.PlaySound("ice_cubes.wav", winsound.SND_ASYNC)

    # Paddle and Ball collisions:
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("boop.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("boop.wav", winsound.SND_ASYNC)



turtle.done()