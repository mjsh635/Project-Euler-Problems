"""The sum of the squares of the first ten natural numbers is,

12+22+...+102=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)2=552=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def Sum_Of_Squares_Difference(range_size):
    """
    Take a range of numbers and return the difference between
    the sum of squares and the squar of the sum

    Parameters:
    range (int) : range of numbers to use, including number

    Return:
    int : returns the difference of squares sumed and sum squared

    """
    # Start both at 0
    squares_summed = 0
    sum_squared = 0

    # Run through all the numbers in that range including the end
    # number
    for num in range(range_size+1):
        # Square each number and add to previous to get a sum of all
        # the squared numbers
        squares_summed += (num*num)
        # Just add the numbers to be squared at the end
        sum_squared += num
    # Finally square the sum
    sum_squared = sum_squared*sum_squared
    # Return the difference
    return sum_squared - squares_summed

print(Sum_Of_Squares_Difference(100))