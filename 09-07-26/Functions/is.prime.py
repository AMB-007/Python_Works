# define a function to check the given number is prime or not

def is_prime(num_1):
    
    for i in range(2,num_1):
        if num_1 % i == 0:
            print("not prime")
            break


    else:
        print("prime")
is_prime(7)



