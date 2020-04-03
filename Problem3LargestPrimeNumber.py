"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"
"""

import math

def Largest_Prime_Factors(number):
    """ Return the larges prime factor of inputed number.

    Parameters:
    number (int): number to be factored

    Return:
    int: returns the largest prime number
    """
    # Starting with a max prime of 1
    max_prime = 1 

    # Keep dividing it evenly until it can't be divided
    # any further
    while number % 2 == 0:
        number = number / 2

    # Having checked all even numbers, check all odd numbers
    # starting with 3 until an even division is found. Then
    # check the new divided number with the remainder of the
    # range.
    for pot_factor in range(3, int(math.sqrt(number)+1), 2):
        while number % pot_factor == 0:
            max_prime = pot_factor
            number = number / pot_factor

    # Return the max prime calculated above        
    return max_prime

print(Largest_Prime_Factors(600851475143))