def is_prime(x):
    if 0>x or x>1000:
        return 'Нет.'
    else:
        k = 0
        for i in range(2, x // 2+1):
            if (x % i == 0):
                k = k+1
        if (k <= 0):
            return 'true'
        else:
            return 'false'
x=int(input()) 
print(is_prime(x)) 