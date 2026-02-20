# Fibonacci sequence using recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) # Recursive call to sum the two preceding numbers until reaching the base cases of n == 0 or n == 1.
    
print(fibonacci(0))  # Output: 0
print(fibonacci(1))  # Output: 1
print(fibonacci(6))  # Output: 8
print(fibonacci(10)) # Output: 55
print(fibonacci(15)) # Output: 610