import turtle

def drawCurve(turtle,l,n):
    if n == 0:
        turtle.forward(l)
        return
    else:
        l/= 3
        drawCurve(turtle,l,n-1)
        turtle.left(60)
        drawCurve(turtle,l,n-1)
        turtle.right(120)
        drawCurve(turtle,l,n-1)
        turtle.left(60)
        drawCurve(turtle,l,n-1)

turtle.setup(650, 400)
"""turtle.speed(0)
turtle.tracer(100,0)"""
drawCurve(turtle, 300,2)
turtle.exitonclick()
