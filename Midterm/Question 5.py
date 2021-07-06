# Write a function called general_poly, that meets the specifications below.
# For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because
# 1 * 10**3 + 2 * 10**2 + 3 * 10**1 + 4 * 10**0


def general_poly(L):
    def innerfunct(x):               # Question asks for return to be a function
        sum = 0                      # Holder for answer
        for i in range(0, len(L)):   # Increments each item in list L
            k = (len(L)-1) - i       # Gives the value for the decreasing exponent of X
            sum += (L[i] * (x**k))   # Adds each number in sections going up the list
        return sum
    return innerfunct




# Test Inputs (List, X)
# ([1,2,3,4,1,2,3,4])(10) = 12341234;
# ([1,2,3,4])(0) = 4;
# ([1,2,3,4])(-7) = -262;
# ([5,6,7,8,9])(28) = 3210713;
# ([103, 42, -78, -3.26])(9) = 77783.74
