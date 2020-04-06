"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import math
def Smallest_Multiple_inefficient(start,stop):
    """
    Return the smallest positive number that is evenly divisible
    by all the numbers from the range inputed

    Parameters:
    start (int): starting number of range, inclusive
    stop (int) : stopping number of range, inclusive

    Returns:
    (int): returns the smallest positive number 
    """

    for range_num in range(stop, math.factorial(stop), stop):
        checked_nums = 0
        for num in range(start,stop + 1):
            if range_num % num == 0:
                checked_nums += 1
                if checked_nums == stop:
                    return range_num

def Smallest_Multiple_Efficient(start,end):
    """
    Return the smallest positive number that is evenly divisible
    by all the numbers from the range inputed

    Parameters:
    start (int): starting number of range, inclusive
    stop (int) : stopping number of range, inclusive

    Returns:
    (int): returns the smallest positive number 
    """

    prime_product = 1
    list_of_primes = [2]
    # Find all the primes in a range of numbers
    for pot_prime in range(2,end+1):
        if pot_prime % 2 != 0:
            if pot_prime not in list_of_primes:
                checked = 0
                for prime in list_of_primes:
                    if pot_prime % prime != 0:
                        checked += 1
                        if checked == len(list_of_primes):
                            list_of_primes.append(pot_prime)
                            break
                    else:
                        break

    # Multiply primes together
    for primes in list_of_primes:
        prime_product *= primes

    # Find n value that makes the equation:
    # Value = prime_product * n
    # Value is valid if divisible by all numebrs in range
    for n in range(1, prime_product):
        value = prime_product * n
        checked_nums = 0
        for num in range(start,end + 1):
            if value % num == 0:
                checked_nums += 1
                if checked_nums == end:
                    return value
print("Largest number evenly divisible by all numbers in range: ",math.factorial(20))
print("The smallest is: ",Smallest_Multiple_Efficient(1,20))