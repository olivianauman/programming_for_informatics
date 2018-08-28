#AUTHOR Olivia Nauman
#Homework Assignment 3 Problem 1
#Programming for Informatics

def count_vowels(filename):
    #read in file, this type of read in develops a list with each line being a list entry
    f = open(filename,'r')
    readFile = f.readlines()
    #vowels is a list of all vowels (uppercase and lowercase) to compare with the values in the lines
    vowels = 'aeiouAEIOU'
    #This is a list where I will add the number of vowels per line, which will have correlating indix values to readFile
    vowelList = []
    #https://stackoverflow.com/questions/3989016/how-to-find-all-positions-of-the-maximum-value-in-a-list
    #I used this stock overflow hint to figure out how to get multiple max indices
    #For each line in the file of lines
    for element in readFile:
        #count the number of vowels in each line up and append it to the blank list
        vowelList.append(element.count("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"))
    #maxLine is all of the numbers that are largest in vowelList(the list of line vowel counts
    maxLine =(max(vowelList))
    #maxIndex keeps track of the index of these max values in order to reference them to print the string they belong to
    maxIndex = vowelList.index(maxLine)
    #print the line with the most vowels and number of vowels in it
    print (readFile[maxIndex] + " " + maxLine)
    #close the file
    f.close()
                               
                               
