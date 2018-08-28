#Olivia Nauman
#Homework 2 Problem 1
#Programming for Informatics

def Bisect():
    #these are markers showing the beginning and the end positions we are viewing on the list throughout the bisection
    start = 0
    end = 25   
    #this is the lowercase alphabet in a list which then can be used to reference indexes
    the_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #this counter assures only 4 tries are used
    counter = 0
    #this is where we currently are at in the list
    the_place = len(the_alphabet)//2
    #this relates this index to the letter equivelant
    my_guess = the_alphabet[the_place]
    #print the first guess and ask the user if their value is the same, higher or lower
    print('Initial guess: {}'.format(my_guess))
    feedback = input("If your letter is: \nthe same as my guess, enter 1 \nhigher,enter 2 \nlower, enter 3: ") 
    #while the values are not equal, we are within range and the guesses are 4 or less...
    while not(feedback == 1) and (start<end) and (counter <= 4):
        #if the letter is closer to a
        if feedback == 2:
            #increment counter for guesses
            counter += 1            
            #update place in the list
            the_place = (start+the_place)//2
            #relate this place to a letter value to be your guess and print it and compare back to the users letter
            my_guess_high = the_alphabet[(the_place)]
            print('Next guess: {}'.format(my_guess_high))
            feedback = input("If your letter is: \nthe same as my guess, enter 1 \nhigher,enter 2 \nlower, enter 3: ") 
            #no more than three guesses
            if counter == 4:
                return ('Game is lost! Too many guesses!')
        #if the letter is closer to z
        if feedback == 3:
            #increment counter for guesses
            counter += 1
            #update range of list being worked with
            the_place = (end+the_place)/2
            #relate this place to a letter value to be your guess and print it and compare back to the users letter
            my_guess_low = the_alphabet[(the_place)]
            print('Next guess: {}'.format(my_guess_low))
            feedback = input("If your letter is: \nthe same as my guess, enter 1 \nhigher,enter 2 \nlower, enter 3: ")
            #no more than three guesses
            if counter == 4:
                return ('Game is lost! Too many guesses!')
    #if the user says that your guess is the same as their letter (1) then print that they have won and in how many guesses!
    if feedback == 1:
        counter = counter + 1
        print ('Yay! You won the game in {} guesses!'.format(counter))
            