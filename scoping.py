#Watch how the local variable trumps the global

x=34
y=99

def inc_x_dec_y(x,y):
    x += 1
    print('x updated within function: {}'.format(x))
    y -= 1
    print('y updated within function: {}'.format(y))
    return x, y

print('Original x, and y: {}, {}'.format(x,y))
x1, y1 = inc_x_dec_y(x,y)
print('Returned x1, and y1: {}, {}'.format(x1, y1))
print('Original x, and y: {}, {}'.format(x, y))

