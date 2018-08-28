#AUTHOR Olivia Nauman
#Homework Assignment 3 Problem 2
#Programming for Informatics
import string

#This program takes the filename and the number of letters each letter should be moved as input
def klingon_poem(filename,n):
    #read in file
    f = open(filename,'r')
    #Make the entire file lowercase
    lowercase_f = f.lower()
    #This variable keeps track of what letter needs to be adjusted  
    WhereYaAt = 0
    #This list will allow us to adjust each letter by n letters
    alphabetList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    #for every character in the file
    for character in lowercase_f:
        #if the character is not a letter, leave it be
        if character in lowercase_f not in alphabetList:
            character = character
        #if the character is a letter...
        elif character in lowercase_f in alphabetList:
            #find where the letter is in the alphabet list (index)
            WhereYaAt = lowercase_f.index(character)
            #for every letter in the file, replace the letter with the letter n letters away in the alphabet
            lowercase_f = lowercase_f.replace(alphabetList[WhereYaAt],alphabetList[WhereYaAt + n]
    #print the new file
    print (lowercase_f)
    #close the file
    f.close()
    
    
    
    
