
print("Welcome to the factorial calculator!\n" "We convert n! to it's numerical value.")
n = input("n?")
while True:
    Should_restart = input("Should we calculate  " + n + "! ?")
    if Should_restart == "yes" or Should_restart == "sure" or Should_restart == "yeah":
        break
    else:
        print("We are having some problem! Please try again!")
        n = input("n?")
        continue
copy_of_n = n
n = int(n)
factorial_of_n = 1
while n >= 1:
    factorial_of_n *= n
    n -= 1
print("the factorial of "+ str(copy_of_n) + " is " + str(factorial_of_n))