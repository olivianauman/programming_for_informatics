#the function bisection takes two parameters, a range of sequential integers
#starting from 0 and an integer n. It returns whether n is found or not found
#in the list and the number of calls made to the function
numberOfCalls = 0
def bisection(numbers, n):
    global numberOfCalls
    numberOfCalls += 1
    #numberOfCalls counts the number of call made to the bisection function
    #This variable will keep track of where we are in the list
    low= 0
    high = len(numbers) - 1
    listLocation = ((low + high)//2)
    #we start with the base case
    if len(numbers) == 0:
        return "Not Found", numberOfCalls
    if numbers[listLocation] == n:
        return "Found " + str(numberOfCalls)
    else: 
        #if the middle value is less than the number we are
        #searching for, shift search higher and increment our call
        #counter
        if numbers[listLocation] < n:
            return bisection(numbers[listLocation+1:], n)
        #if the middle value is more than the number we are
        #searching for, shift search lower and increment our call
        #counter        
        elif numbers[listLocation] > n:
            return bisection(numbers[:listLocation], n)
bisection(list(range(10)), 1)
    
    
    
    