def raise_power(mantissa_list, exponent):
    '''
    This function takes in a list of numbers and an exponent.
    It calculates the sum of the numbers raised to the exponent.
    '''
    res = 0;
    for i in mantissa_list:
        res += i ** exponent
    return res

def answer(input_list):
    '''
    This function takes in a list of numbers and returns the sum
    of its cubes
    '''
    return raise_power(input_list, 3)
    
