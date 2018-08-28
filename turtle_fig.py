#import turtles to utilize its functions
import turtle

def turtle_fig():
    #set the window dimensions
    turtle.setup(850,850)
    #set variable to reference the screen
    window = turtle.Screen()
    #set screen color
    window.bgcolor('hotpink')
    #get turtle
    fun_maker = turtle.getturtle()
    #make the turtle into a turtle shape
    fun_maker.shape("turtle")
    #make writing light blue
    fun_maker.pencolor('darkblue')
    #put the pen up and set the turtle at the starting point
    fun_maker.penup()
    fun_maker.right(270)
    fun_maker.forward(350)
    #reorientate the turtle and put the pen down to begin forming the "F"
    fun_maker.right(270)
    fun_maker.pendown()
    fun_maker.forward(100)
    fun_maker.right(270)
    fun_maker.forward(200)
    fun_maker.right(180)
    fun_maker.forward(100)
    fun_maker.right(90)
    fun_maker.forward(75)
    #put the pen up and reorientate. Put the pen down to begin forming the "U"
    fun_maker.penup()
    fun_maker.forward(75)
    fun_maker.right(90)
    fun_maker.pendown()
    fun_maker.forward(100)
    fun_maker.right(270)
    fun_maker.forward(75)
    fun_maker.right(270)
    fun_maker.forward(100)
    #put the pen up an dreorientate. Put the pen down to begin forming the "N"
    fun_maker.penup()
    fun_maker.forward(15)
    fun_maker.right(90)
    fun_maker.forward(75)
    fun_maker.right(90)
    fun_maker.pendown()
    fun_maker.forward(115)
    fun_maker.right(180)
    fun_maker.forward(100)
    fun_maker.right(90)
    fun_maker.forward(75)
    fun_maker.right(90)
    fun_maker.forward(100)
    #put the pen up and reorientate to begin the star!!
    fun_maker.penup()
    fun_maker.forward(150)
    fun_maker.right(90)
    fun_maker.forward(150)
    fun_maker.pendown()
    # I found this portion of the program at https://michael0x2a.com/blog/turtle-examples
    # I think it is really interesting! 
    for i in range(20):
        fun_maker.forward(i*10)
        fun_maker.right(144)
    turtle.exitonclick()
    
    
    