#Olivia Nauman
#Homework 10 Part 2

#I will use this later to reference pi
import math

#parent class
class Shape(object):
    #initialize both the x and y cooordinate
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        
    #get the x coordinate with this function    
    def get_x_coordinate(self):
        return self.x_coordinate
    
    #get the y coordinate with this function
    def get_y_coordinate(self):
        return self.y_coordinate
    
    #set the x coordinate with this function
    def set_x_coordinate(self, x):
        self.x_coordinate = x
    
    #set the y coordinate with this function    
    def set_y_coordinate(self,y):
        self.y_coordinate = y
    
    #this function will allow for the coordinate to move... mx is the movement of x and my is the movement of y
    def movement(self, mx, my):
        self.x_coodinate += mx
        self.y_coordinate += my
        
#subclass 1: squares
class Squares(Shape):
    
    #the child class squares has a particular way to find areas
    def __init__(self, side):
        self.side = side 
        
    #this function gets the value of the side 
    def get_side(self):
        return self.side
    
    #this function sets a new length to the side
    def set_side(self, side):
        self.side = side   
                
    #we know that the area of a square is defined by side * side
    def area(self):
        return float(self.side)**2    
 
    
    
    
#subclass 2: squares
class Circles(Shape):
    
    #the child class circles has a particular way to find areas
    def __init__(self, radius):
            self.radius =  radius
    
    #this function returns the radius        
    def get_radius(self):
        return self.radius
    
    #this function sets a new value to the radius        
    def set_radius(self, radius):
        self.radius = radius
            
    #we know that the area of a circle is defined by pi * (r^2)... pi in python can be used by saying math.pi after the math library is imported, which I have done.
    def area(self):
        return math.pi * (float(self.radius)**2)
    
C1 = Circles(2)
C1A = C1.area
C2 = Circles(3)
C2A = C2.area
S1 = Squares(1)
S1A = S1.area
S2 = Squares(13.5)
S2A = S2.area
print("Individual Areas: " + str(C1A()),", ", str(C2A()),", ", str(S1A()),", ", str(S2A()))
print("Total Area: " + str(float(C1A()) + float(C2A()) + float(S1A()) + float(S2A())))


    
