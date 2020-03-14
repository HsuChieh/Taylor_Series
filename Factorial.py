def factorial(n):
    n = int(n)
    factorial_of_n = 1
    while n >= 1:
        factorial_of_n *= n
        n -= 1
    print(factorial_of_n)

