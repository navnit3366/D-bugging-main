from turtle import *
import time
import random

score = 0
delay = 0.1

root = Screen()
root.title('Snake Game')
root.setup(width=600, height=600)
root.bgcolor('black')
root.bgpic('border.gif')
root.addshape('body.gif')
root.addshape('downmouth.gif')
root.addshape('upmouth.gif')
root.addshape('leftmouth.gif')
root.addshape('rightmouth.gif')
root.addshape('food.gif')

root.tracer(False)

head = Turtle()
head.shape('upmouth.gif')
head.color('black')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

food = Turtle()
food.shape('food.gif')
food.color('orange')
food.penup()
food.goto(0, 100)

segments = []
pen = Turtle()

pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 268)
pen.write('Score:0', align='center', font=('courier', 25, 'bold'))


def go_down():
    if head.direction != 'up':
        head.direction = 'down'
        head.shape('downmouth.gif')


def go_up():
    if head.direction != 'down':
        head.direction = 'up'
        head.shape('upmouth.gif')


def go_left():
    if head.direction != 'right':
        head.direction = 'left'
        head.shape('leftmouth.gif')


def go_right():
    if head.direction != 'left':
        head.direction = 'right'
        head.shape('rightmouth.gif')


def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)


root.listen()
root.onkeypress(go_up, "Up")
root.onkeypress(go_down, 'Down')
root.onkeypress(go_left, 'Left')
root.onkeypress(go_right, 'Right')

while True:
    root.update()

    if head.xcor() > 255 or head.xcor() < -260 or head.ycor() > 260 or head.ycor() < -260:
        t = Turtle()
        t.goto(0, 0)
        t.color('orange')
        t.penup()
        t.hideturtle()
        t.write('Game Lost', align='center', font=('courier', 34, 'bold'))
        time.sleep(1)
        t.clear()

        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        score = 0
        delay = 0.1

        pen.clear()
        pen.write(f'Score:{score} ', align='center', font=('courier', 25, 'bold'))

    if head.distance(food) < 20:
        x = random.randint(-255, 255)
        y = random.randint(-255, 255)
        food.goto(x, y)
        delay -= 0.003

        new_segment = Turtle()
        new_segment.shape('body.gif')
        new_segment.color('grey')
        new_segment.penup()
        segments.append(new_segment)

        score = score + 10

        pen.clear()
        pen.write(f'Score:{score}', align='center', font=('courier', 25, 'bold'))

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f'Score:{score} ', align='center', font=('courier', 25, 'bold'))

    time.sleep(delay)