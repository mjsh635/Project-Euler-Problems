""" (Problem 1, Multiples of 3 and 5)

If we list all the natural numbers below 10 that 
are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def Sum_Of_Multiples(multiples,low_range,high_range):
    """ Return the sum of the multiples between low_range and high_range.
        

        Parameters:
        multiples (int[]): list of integers for multiples
        low_range (int): starting number, inclusive
        high_range (int): ending number, exclusive
        
        Returns:
        int: sum of multiples
    """
    sum = 0
    for num in (range(low_range,high_range)): # Check each number in range
        for mult in multiples: # Check each multiple
            if num % mult == 0: # If number has a multiple
                sum += num # Add to total
                break # If a multiple is found, break multiple check

    return sum # Return the total


print(Sum_Of_Multiples([3,5],1,1000))

