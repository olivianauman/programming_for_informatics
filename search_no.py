import random
#create a range, then store in in a list
range_of_numbers = list(range(0, 20))
number_to_search = 5
start = 0
end = len(range_of_numbers) - 1
#generate the index for the first guess randomly
current = random.randint(start, end)
# get the ACTUAL value of the guess from the list of numbers
current_number = range_of_numbers[current]
print('Initial guess: {}'.format(current_number))
print('{}'.format(range_of_numbers[start:end]))
while not(current_number == number_to_search) and start<end:
    if number_to_search < current_number:
        start = start
        end = current - 1
        current = (start + end)// 2
        current_number = range_of_numbers[current]
        print('Next guess: {}'.format(current_number))
    elif number_to_search > current_number:
        start = current + 1
        end = end
        current = (start+end)//2
        current_number = range_of_numbers[current]
        print('Next guess: {}'.format(current_number))
        
print('I either found the number, or violated the start < end condition: {}, {}, {}'.format(current_number, start, end))
