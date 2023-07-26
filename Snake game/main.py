import time
from turtle import *
import random
score=0
execution_delay=0.1

a=Screen() #object of Screen class

a.title('Snake Game')
a.setup(width=600,height=600)
a.bgcolor('Yellow')
a.bgpic('border.gif')
a.tracer(False)
a.addshape('upmouth.gif')
a.addshape('food.gif')
a.addshape('downmouth.gif')
a.addshape('rightmouth.gif')
a.addshape('leftmouth.gif')
a.addshape('body.gif')

head=Turtle()
head.shape('upmouth.gif')
head.penup()
head.goto(0,0)
head.direction='stop'

food=Turtle()
food.penup()
food.goto(0,100)
food.shape('food.gif')
segments =[]
text=Turtle()
text.penup()
text.goto(0,268)
text.hideturtle()
text.color('white')
text.write('Score:0',font=('courier',25,'bold'),align='center')

Lost=Turtle()
Lost.color('Red')
Lost.penup()
Lost.hideturtle()

def move_snake():
     if head.direction=='up':
          y=head.ycor()
          y=y+20
          head.sety(y)

     if head.direction=='down':
          y=head.ycor()
          y=y-20
          head.sety(y)
     if head.direction=='right':
          x=head.xcor()
          x=x+20
          head.setx(x)
     if head.direction=='left':
          x=head.xcor()
          x=x-20
          head.setx(x)

def go_up():
  if head.direction!='down':
          head.direction='up'
          head.shape('upmouth.gif')

def go_down():
  if head.direction!='up':
          head.direction='down'
          head.shape('downmouth.gif')

def go_right():
  if head.direction!='left':
          head.direction='right'
          head.shape('rightmouth.gif')

def go_left():
  if head.direction!='right':
          head.direction='left'
          head.shape('leftmouth.gif')


a.listen()
a.onkeypress(go_up,'Up')
a.onkeypress(go_right,'Right')

a.onkeypress(go_down,'Down')
a.onkeypress(go_left,'Left')

while True:
     a.update()

     if head.xcor()>260 or head.xcor()<-260 or head.ycor()>260 or head.ycor()<-260:
          Lost.write('Game Over', align='center',font=('Algerian',38,'bold'))
          time.sleep(1.5)
          Lost.clear()
          time.sleep(1)
          head.goto(0,0)
          head.direction='Stop'
          for bodies in segments:
          bodies.goto(1000,1000)
          score=0
          execution_delay=0.1
          segments.clear()
          text.clear()
          text.write('score:0',align='center',font=('courier',25,'bold'))

     if head.distance(food)<20:
          x=random.randint(-255,255)
          y=random.randint(-255,255)
          food.goto(x,y)
          execution_delay=execution_delay-0.003
          body=Turtle()
          body.penup()
          body.shape('body.gif')
          segments.append(body)
          score=score+5
          text.clear()
          text.write(f'Score:{score}',font=('courier',25,'bold'),align='center')

     for i in range(len(segments)-1,0,-1):
          x=segments[i-1].xcor()
          y=segments[i-1].ycor()
          segments[i].goto(x,y)

     if len(segments)>0:
          x=head.xcor()
          y=head.ycor()
          segments[0].goto(x,y)

     move_snake()

     for bodies in segments:
          if bodies.distance(head)<20:
              time.sleep(1)
              head.goto(0,0)
              head.direction='stop'

              for bodies in segments:
                  bodies.goto(1000,1000)

                  segments.clear()
                  score=0
                  execution_delay=0.1
                  Lost.write('Game Over', align='center', font=('Algerian', 38, 'bold'))
                  time.sleep(1)
                  Lost.clear()
                  text.clear()
                  text.write('score:0', align='center', font=('courier',25,'bold'))


     time.sleep(execution_delay)
