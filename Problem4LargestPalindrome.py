"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def Largest_Palindrome_Product(digits):
    """ Take in requested digit number and return the largest
    produceable palindrome from those numbers

    Parameters: 
    digits (int) : number to 

    Returns:
    int : largest palindrome
    """
    # start with 1
    largest_palindrome = 1
    # In a range of 0-10^digits, check if product is equal to reverse of result
    for num1 in range(10**digits):
        # After each step, stop checking numbers already looked at
        for num2 in range(num1,10**digits):
            product = num1 * num2
            # check the reverse of the product
            productRev = str(product)[::-1]
            # If it matches in reverse, it's a palindrome
            # Check againsts previous palindromes, only saving the largest
            if (product == int(productRev)) and (int(productRev) > largest_palindrome):
                largest_palindrome = int(productRev)
       
    # Return the value
    return largest_palindrome
                

print(Largest_Palindrome_Product(3))