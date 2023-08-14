import turtle
wn = turtle.Screen()
jim = turtle.Turtle()

side = int(input("How many sides is the polygon?"))
angle = 360 / side
for _ in range(side):
    jim.forward(100)
    jim.left(angle)
