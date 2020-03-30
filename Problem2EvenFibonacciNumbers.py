""" (Problem 2, Even Fibonacci numbers)
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def Even_Fibonacci(end_value):
    """ Sum all of the even-valued terms in the fibonacci sequence

    Parameters:
    end_value (int): The highest value term value the check until

    Return:
    (int): returns the summation of the even-values
    """
    sum = 0
    fib_cur_value = 1 
    fib_pre_value = 0
    while fib_cur_value < end_value: # Limit the value to requested amount
        fib_next_value = fib_pre_value + fib_cur_value # Next num is current + previous
        if fib_cur_value % 2 == 0: # Add the current value if even
            sum += fib_cur_value 
        fib_pre_value = fib_cur_value # Previous value is set to current
        fib_cur_value = fib_next_value # Current value is set the next

    return sum # Return the sum of all the even numbers

print(Even_Fibonacci(4000000))