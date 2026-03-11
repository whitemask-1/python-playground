result = 0
for i in range(1,889000,2):
    i = i**2
    result += i

print(result)

def sumOddSquares(n):
    return (n*((2*n)+1)*((2*n)-1)) / 3

print(sumOddSquares(444500)
