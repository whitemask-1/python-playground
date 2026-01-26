#Number pattern function from freeCodeCamp Python curriculum

def number_pattern(n):
    pattern = ''
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    elif n < 1:
        return 'Argument must be an integer greater than 0.'
    for num in range(1,n+1):
        pattern += str(num)
        if num != n:
            pattern += ' '
    
    return pattern

print(number_pattern(8))