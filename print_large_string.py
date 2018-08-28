def print_large_string(input_string, max_length):
    #current_string keeps track of the present string as we continue to append 
    #it to itself
    current_string = input_string
    #base case is the string being max_length or greater in length, if this is the case, cut to the chase and tell the user 
    #and print the string and the length of the string
    if len(current_string) >= max_length:
        print("Length reached!")
        print( current_string + " " + str(len(current_string)))
    #Otherwise print the current string and the length of that string until the string is larger than or equal to the max_length    
    else:
        while len(current_string) <= max_length:
            print (current_string + " " + str(len(current_string)))
            current_string = current_string + input_string
            #call on the function to eventually reach length
            return (print_large_string(current_string, max_length))
            
    