# turtle trys
import turtle # set window size 
turtle.setup(800,600)
# get reference to turtle window 
window = turtle.Screen()
# set window title bar 
window.title("making a shape")
# set background color 
window.bgcolor('purple')
the_turtle = turtle.getturtle()  
# default turtle # 3 attributes: positioning, heading (orientation), pen
# creating a box with relative positioning 
the_turtle.hideturtle() 
# to see the turtle or not to see. #the_turtle.forward(100) # relative positioning
#  the turtle starts by looking to the right (0 degrees) 
the_turtle.setposition(100, 0) 
# absolute positioning the_turtle.left(90)  # turning 90 degrees to the left #the_turtle.setheading(135) # explicitly lookig in the 90 deg angle # see what happends when you change 90 above to something else 
the_turtle.forward(100) 
the_turtle.left(90) 
the_turtle.forward(100) 
the_turtle.left(90) 
the_turtle.forward(100) 
the_turtle.left(90)
# exit on close window 
turtle.exitonclick()