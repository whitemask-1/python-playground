# We can use recursion to calculate the factorial of a number with efficiency that cant be matched without recursion.

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1) # The function calls itself here and multiplies n by the factorial of (n-1) until reaching n == 1 or 0 which then returns 1 and ends the recursion.
    
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
print(factorial(1))  # Output: 1
print(factorial(6))  # Output: 720

# Heres the function even more streamlined using a single line return statement with a conditional expression.
def factorial_streamlined(n):
    return 1 if n==0 or n==1 else n * factorial_streamlined(n-1)

print(factorial_streamlined(5))  # Output: 120
print(factorial_streamlined(0))  # Output: 1
print(factorial_streamlined(1))  # Output: 1
print(factorial_streamlined(6))  # Output: 720

# Python also has a built in for factorials but its good to understand how recursion can be used to solve problems like this.
from math import factorial as math_factorial
print(math_factorial(5))  # Output: 120
print(math_factorial(0))  # Output: 1
print(math_factorial(1))  # Output: 1
print(math_factorial(6))  # Output: 720