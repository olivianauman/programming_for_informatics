#Olivia Nauman
#Programming for Informatics
#Homework 1
#August 27, 2016

#This program takes the diameter of a circle and returns the area of the circle to the user, possibly converting unites to do so.
#We must first import math so that we are able to later use pi
import math
def circleArea():
    #input_diameter is a variable that asks the user for the diameter of the circle
    input_diameter = float(input("What is the diameter of the circle without units?"))
    #what_type is a variable that asks the user for the data type(feet or inches)
    what_type = str(input("Is this diameter in inches or feet?"))
    area_feet = math.pi * ((input_diameter / 2)**2)
    area_inches = math.pi * (((input_diameter/10)**2)) 
    if str(what_type) == "feet":
        return "Area of the circle with a diameter of " + str(input_diameter) + " "+ what_type + " is " + str(area_feet) + " square feet."
    elif str(what_type) == "inches":
        return "Area of the circle with a diameter of " + str(input_diameter) + " "+ what_type + " is " + str(area_inches) + " square feet."
    else:
        return "You did not appropriately answer the questions. Try again."
    
    


    

                               