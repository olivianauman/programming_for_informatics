#here is one way to use try except
def division(number,other):
    try:
        x = number / other
        return x
        
    except ZeroDivisionError as e:
        print (e)
        
#You can also do it like this, but you need to use your own error notice!        
def division_alt(number,other):
    try:
        x = number / other
        return x
        
    except ZeroDivisionError:
        print ("Division by Zero! OH NO!")
        
        
#Assertion
def divide_3(number, other):
    x = number / other
    assert other != 0, "Can't Divide by Zero!"
    return x

def tuplePractice():
    tuplestuff = (1,2,3,4,5,6,7)
    x = tuplestuff[3]
    return x