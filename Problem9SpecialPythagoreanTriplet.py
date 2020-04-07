"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def Special_Pythagorean_Triplet():
    """
    Find the Pythagorean Triplet that solves the above problem

    Parameters:
    none 

    Return:
    int : the product of a * b * c

    """
    a = 1
    b = 1
    c = 1
    for a in range(1,1000):
        for b in range(1,1000):
            for c in range(1,1000):
             # Conditions for a Pythagorean Triplet
                if (a < b) and (b < c):
                    if ((a*a) + (b*b)) == (c*c):
                        # Check if a+b+c = 1000
                        if (a + b + c) == 1000:
                            # Return the product
                            print(a,b,c)
                            return a*b*c
        print("Percent Complete:", (a/1000)*100,end='\r' )              

print("\n",Special_Pythagorean_Triplet())