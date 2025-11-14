
def sum_of_primes(n):
    if n == 0:
        return 0
    else:
        return (n+sum_of_primes(n-1))
    
n = int(input("Enter an integer: "))
print(n)
print("ths sum of primes is : ", sum_of_primes(n))
