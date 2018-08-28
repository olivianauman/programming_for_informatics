#AUTHOR Olivia Nauman
#Homework Assignment 3 Problem 3
#Programming for Informatics
import string

def transform_input(filename):
    #read in file
    f = open(filename,'r')
    #make a list of the individual file lines
    readFile = f.readlines()
    #remove all occurances of 't' or 'T'
    for line in readFile:
        line.replace("t","")
        line.replace("T","")
        #replace all punctuation with a whitespace
        if character in string.punctuation:
            line = line.replace(character," ")
    #calculates the number of letters in each line and then prints it at the end of the line
    for line in readFile:
        print (line + (len(line) - line.count(' '))
    #close the file
    f.close()
