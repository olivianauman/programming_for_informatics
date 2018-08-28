import time
import random
#time is a library which will later allow me to insert a pause
def binarySearch():
    #ask the user to think of any lowercase letter
    print "Think of a letter (a-z). You may even think of a or z."
    #I will then use the listed alphabet to preform a binary search
    the_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #allow the user 2 seconds to think of a letter
    time.sleep(2)
    #the guess is each half of the previous list, beginning with the halfway point, and proceeding accordingly
    my_guess1 = the_alphabet[random.randrange(0,25)]
    #tell the user your guess and ask for input on whether this value is the same, higher, or lower
    print "My guess is " + my_guess1 +". "
    comparison_one = input("If your letter is: \nthe same as my guess, enter 1 \nhigher,enter 2 \nlower, enter 3: ")
    #if input is 1 then the game is won
    if comparison_one == 1:
        return "Yay! Game won in 1 guess!"
    #if input is 2, we move to the 1/4 point of the total list for the second guess and then compare again
    elif comparison_one == 2:  
        my_guess2 = the_alphabet[(len(the_alphabet)/4)]
        print "My guess is " + my_guess2 + "."
        comparison_two = input("If your letter is: \nthe same as my guess, enter 1 \nhigher,enter 2 \nlower, enter 3: ")
        #if input is 1 the game is won
        if comparison_two == 1:
            return "Yay! Game won in 2 guesses!"
        #if input is 2 we move to the 7/8 point in the list
        elif comparison_two == 2:
            my_guess3 = the_alphabet[(len(the_alphabet)/8)]
            print "My guess is " + my_guess3 + "."
            comparison_three =  input("If your letter is: \nthe same as my guess, enter 1 \nhigher,enter 2 \nlower, enter 3: ")
            if comparison_three == 1:
                return "Yay! Game won in 3 guesses!"
            elif comparison_three == 2:
                my_guess4 = the_alphabet[(len(the_alphabet)/16)]
                print "My guess is " + my_guess4 + "."
                comparison_four = input("If your letter is: \nthe same as my guess, enter 1 \nhigher, enter 2 \nlower, enter 3: ")
                if comparison_four == 1:
                    print "Yay! Game won in 4 guesses!" 
                else:
                    print "Game is lost!"
            elif comparison_three == 3:
                my_guess4 = the_alphabet[(len(the_alphabet)/16) * 3]
                print "My guess is " + my_guess4 + "."
                comparison_four = input("If your letter is: \nthe same as my guess, enter 1 \nhigher, enter 2 \nlower, enter 3: ")
                if comparison_four == 1:
                    print "Yay! Game won in 4 guesses!" 
                else:
                    print "Game is lost!"                
        #if input is 3 we move to the 3/8 point in the list
        elif comparison_two == 3:
            my_guess3 = the_alphabet[(len(the_alphabet)/8) * 3]
            print "My guess is " + my_guess3 + "."
            comparison_three =  input("If your letter is: \nthe same as my guess, enter 1 \nhigher,enter 2 \nlower, enter 3: ")
            if comparison_three == 1:
                return "Yay! Game won in 3 guesses!"
            elif comparison_three == 2:
                my_guess4 = the_alphabet[(len(the_alphabet)/16)* 5]
                print "My guess is " + my_guess4 + "."
                comparison_four = input("If your letter is: \nthe same as my guess, enter 1 \nhigher, enter 2 \nlower, enter 3: ")
                if comparison_four == 1:
                    print "Yay! Game won in 4 guesses!" 
                else:
                    print "Game is lost!"
            elif comparison_three == 3:
                my_guess4 = the_alphabet[(len(the_alphabet)/16) * 7]
                print "My guess is " + my_guess4 + "."
                comparison_four = input("If your letter is: \nthe same as my guess, enter 1 \nhigher, enter 2 \nlower, enter 3: ")
                if comparison_four == 1:
                    print "Yay! Game won in 4 guesses!" 
                else:
                    print "Game is lost!"                         
    #if input is 3, we move to the 1/4 portion of the list for the second guess and compare again    
    elif comparison_one == 3:
        my_guess2 = the_alphabet[(len(the_alphabet)/4) *3]
        print "My guess is " + my_guess2 + "."
        comparison_two =  input("If your letter is: \nthe same as my guess, enter 1 \nhigher,enter 2 \nlower, enter 3: ")
        if comparison_two == 1:
            return "Yay! Game won in 2 guesses!"  
        elif comparison_two == 2:
            my_guess3 = the_alphabet[(len(the_alphabet)/8) * 5]
            print "My guess is " + my_guess3 + "."
            comparison_three =  input("If your letter is: \nthe same as my guess, enter 1 \nhigher,enter 2 \nlower, enter 3: ")
            if comparison_three == 1:
                return "Yay! Game won in 3 guesses!"
            elif comparison_three == 2:
                my_guess4 = the_alphabet[(len(the_alphabet)/16) * 9]
                print "My guess is " + my_guess4 + "."
                comparison_four = input("If your letter is: \nthe same as my guess, enter 1 \nhigher, enter 2 \nlower, enter 3: ")
                if comparison_four == 1:
                    print "Yay! Game won in 4 guesses!"
                else:
                    print "Game is lost!"
            elif comparison_three == 3:
                my_guess4 = the_alphabet[(len(the_alphabet)/16) * 11]
                print "My guess is " + my_guess4 + "."
                comparison_four = input("If your letter is: \nthe same as my guess, enter 1 \nhigher, enter 2 \nlower, enter 3: ")
                if comparison_four == 1:
                    print "Yay! Game won in 4 guesses!"
                else:
                    print "Game is lost!"  
        elif comparison_two == 3:
            my_guess3 = the_alphabet[(len(the_alphabet)/8) * 7]
            print "My guess is " + my_guess3 + "."
            comparison_three =  input("If your letter is: \nthe same as my guess, enter 1 \nhigher,enter 2 \nlower, enter 3: ")
            if comparison_three == 1:
                return "Yay! Game won in 3 guesses!"
            elif comparison_three == 2:
                my_guess4 = the_alphabet[(len(the_alphabet)/16) * 13]
                print "My guess is " + my_guess4 + "."
                comparison_four = input("If your letter is: \nthe same as my guess, enter 1 \nhigher, enter 2 \nlower, enter 3: ")
                if comparison_four == 1:
                    print "Yay! Game won in 4 guesses!"
                else:
                    print "Game is lost!"
            elif comparison_three == 3:
                my_guess4 = the_alphabet[(len(the_alphabet)/16) * 15]
                print "My guess is " + my_guess4 + "."
                comparison_four = input("If your letter is: \nthe same as my guess, enter 1 \nhigher, enter 2 \nlower, enter 3: ")
                if comparison_four == 1:
                    print "Yay! Game won in 4 guesses!"
                else:
                    print "Game is lost!"             
                
            
    
    
    
    
    
    