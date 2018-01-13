import turtle
  
def draw_square():
  window = turtle.Screen()
  window.bgcolor('red')
  brad = turtle.Turtle()
  brad.shape('arrow')
  brad.color('blue')
  brad.speed(5)
  
  i = 0
  while i < 4:
    brad.forward(100)
    brad.right(90)
    i += 1
  
  window.exitonclick()

def draw_circle():  
  window = turtle.Screen()
  window.bgcolor('red')
  angie = turtle.Turtle()
  angie.shape('turtle')
  angie.color('green')
  angie.circle(100)
  
  window.exitonclick()

def draw_triangle():
  window = turtle.Screen()
  window.bgcolor('red')
  nate = turtle.Turtle()
  nate.shape('square')
  nate.color('yellow')
  i = 0
  while i < 3:
    nate.forward(100)
    nate.right(120)
    i += 1
  
  window.exitonclick()

def draw_circlesquare():
  window = turtle.Screen()
  window.bgcolor('red')
  brad = turtle.Turtle()
  brad.shape('arrow')
  brad.color('blue')
  brad.speed(50)
  
  j = 0
  while j < 36:
    i = 0
    while i < 4:
      brad.forward(100)
      brad.right(90)
      i += 1
    brad.right(10)
    j += 1
  
  window.exitonclick()

draw_circlesquare()  
draw_square()
draw_circle()
draw_triangle()