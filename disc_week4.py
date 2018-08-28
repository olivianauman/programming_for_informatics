def fibonacci(n):
    if n <= 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def exponent(x,n):
    if n == 0:
        return 1
    else:
        return x * exponent(x, n-1)
def permutation(A, current_permutation):
    if len(A) == 0:
        print(current_permutation)
    else:
        for element in A:
            inx = A.index(element)
            new_A = A[:idx] + A[idx+1:]
            permutation(new_A, curremt_permutation + [element])


def change__count(n):
    if n<0:
        return 0
    elif n == 1:
        return 1
    else:
        return change_count(n-1) + change_count(n-5)
    
