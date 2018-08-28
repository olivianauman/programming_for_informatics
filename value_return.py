def multiply3to9(input_number):
    sum = 0
    for to_multiply_with in range(3, 10, 2):
        product = input_number * to_multiply_with
        print(' {} * {} = {:.2f}'.format(input_number, to_multiply_with, product))
        sum += product
    return sum

sum1 = multiply3to9(-2.5)
sum2 = multiply3to9(21)
sum3 = multiply3to9(10.3)
print("{}, {}, {}'.format(sum1 ,sum2, sum3))