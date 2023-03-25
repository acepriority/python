def prime(n):
    if n < 2:
        print(f'{n} is not prime')
    elif n == 2:
        print(f'{n} is the only even prime number')
    
    for i in range(2, n):
        if n % i == 0:
            print(f'{n} is even not prime')
        else:
            return True
            

print(prime(5))

