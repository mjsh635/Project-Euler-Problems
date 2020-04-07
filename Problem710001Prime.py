"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def target_prime(nth_prime):
    """
    Return the nth prime number

    Parameters:
    nth_prime (int): the nth prime number

    Return:
    int : the prime number that is nth 
    """

    list_of_primes = [2]
    pot_prime = 2
    # Find all the primes in a range of numbers
    while (len(list_of_primes) <= nth_prime -1):
        pot_prime += 1
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
        print("Found primes: ",len(list_of_primes),end='\r')
    return list_of_primes[nth_prime-1]

print("\n",target_prime(10001))