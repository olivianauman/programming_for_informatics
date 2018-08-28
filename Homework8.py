#Olivia Nauman
#Homework 8


#Problem 1
def problem_one(list1,list2):
    #initialize an empty list
    newList = []
    #initialize the placekeeper
    element = 0
    try:
        #while there are still elements for comparison
        while element < len(list1):
            #set variable equal to the limst one element divided by the list 2 element times 3
            value = list1[element]/(list2[element] * 3)
            #add the value equal to this variable to the newList
            newList.append(value)
            #increment our place in the list
            element += 1
        #return the newList    
        return newList
    #you can not divide by zero
    except ZeroDivisionError:
        print ("division by zero!") 
    #make sure correct data type is put into parameters    
    except TypeError:
        print ("Type Error!")
    #make sure list comparison is within range    
    except IndexError:
        print("Index Error!")
    #for all other errors return a generic error    
    except:
        print("An error occured!")
        
#Problem 2
def raise_power(mantissa_list, exponent):
    '''
    This function takes in a list of numbers and an exponent.
    It calculates the sum of the numbers raised to the exponent.
    '''
    #if the list is empty, let the user know
    assert len(mantissa_list) != 0, "You have an empty list."
    #if the first input isnt a list let the user know
    assert isinstance(mantissa_list, list), "Your input is of the wrong type! It is supposed to be a list."
    #if the second input isnt an integer let the user know
    assert isinstance(exponent, int), "Your input is of the wrong type! It is supposed to be an integer."
    res = 0;
    #take each element of the list to the power of the second parameter and add it to the resulting count
    for i in mantissa_list:
        res += i ** exponent
     #make sure the result is between 0 and 100 inclusively   
    assert 0 <= res <= 100, "Sum out of range!"   
    return res

def answer(input_list):
    '''
    This function takes in a list of numbers and returns the sum
    of its cubes
    '''
    return raise_power(input_list, 3)
    
        