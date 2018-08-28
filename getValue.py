x=1
y=1

def adding(a, b):
    x=5
    def getValue(x):
        print ('x before reset ', x)
        x=1
        print ('x after reset ', x)
        return x * 3
    return a + getValue(10)

ans = adding(4,5)

print(ans)


def split_string(st):
    '''
    Function splits at a string, on the last vowel and returns the left portion of st.
    If there is no vowel in st, then it returns st.
    '''
    vowels = 'aeiouAEIOU'
    lastVowelPosition = -100
    counter = 0
    for i in st:
        if i in vowels:
            lastVowelPosition = counter 
            counter = counter + 1
            
            print ('string is ', st, 'and last vowel position ', lastVowelPosition)
        if (lastVowelPosition > -100):
            return (st[0:lastVowelPosition])
        else:
            return st
    
    def printit(st):
        for i in st:
            print i
            #This prints each letter of the string on a new line.
    def printit_recursive(st):
        #you must create a base case!
        if len(st) == 1:
            print(st)
        else:
            print(st[0])
            printit_recursive(st[1:])
            
    def factorial(n):
        fact = 1
        for i in range(n,0,-1):
            fact = fact * i
        return fact
    def factorial_recursive(n):
        #you must create a base case
        if n <= 1:
            return (1)
        else:
            return (n * factorial_rec(n-1))
        
    def palindrome_recursive(s):
        if len(s) == 1:
            return True
        else: 
            palindrome(s[1:-1])
            return s[0] == s[1]
        
    def print_st_rec(st):
        ''' prints the string at recursively one char per line '''
        #base case
        if len(st) == 1:
            print(st)
        else:
            #non base case
            print(st[0])
            #this gives everything but the first character
            print_st_rec(st[1:])
            
    def factorial_rec(n):
        #base case
        if n <= 1 :
            return 1
        #non base case
        else:
            return n * factorial_rec(n-1)
        
    def palindrome(st):
        ''' check if string st is a palindrome '''
        #base case
        if len(st) is <= 1:
            return True
        #non base case
        else:
            #0 gives first index and -1 gives the last
            return st[0] == st[-1] and palindrome(st[1:-1])
        
    
            
            
    
    

            

    