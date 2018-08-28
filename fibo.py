#Olivia Nauman
#Homework 10


#initialize both counters to zero
times_called = 0
base_case = 0

def fibonacci(n):
        ''' computes the Fibonacci number for an integer n >= 0 '''
        
        global times_called #this allows the global variable to be passed in
        global base_case # same as above
        #for every time fibonacci is called, times called increases by 1
        times_called += 1
        if n <= 1:
                #for every time the base case is called we increment the counter by one
                base_case += 1
                return 1
        else:
                return fibonacci(n - 1) + fibonacci(n - 2)
fibonacci(5)
print (times_called, base_case) # print both counters
        
        #In the best case (base case), O(1). It will reach the base case and only call fibonacci once!
        #In the worst case, O(2^n) because for every iteration you are doubling the number of calls made


        

         
