"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math

def isprime(potential_prime):
    """Checks if number is a Prime

    Parameters:
    potential_prime (int) : number to be checked

    Return:
    (Bool) : returns True of False if Prime
    """
    if potential_prime == 2:
        return True
    # integers less than 2 and even numbers other than 2 are not prime
    elif potential_prime < 2 or not potential_prime & 1:
        return False
    # loop looks at odd numbers 3, 5, 7, ... to sqrt(n)
    for divisors in range(3, int(potential_prime**0.5)+1, 2):
        if potential_prime % divisors == 0:
            return False
    return True

def Sum_of_Primes(primes_below):
    """Sum all primes below a target number

    Parameters:
    primes_below (int) : inclusive, numbers to check

    Return:
    (int) : returns total sum of primes
    """
    total = 0
    # Check all numbers below target
    for nums in range(primes_below+1):
        # If the number is a prime, add to the total
        if isprime(nums):
            total += nums
    # Return the total
    return total

print(Sum_of_Primes(2000000))
