def FactorialRecursive(nth):
    if nth == 1:
        return 1
    return nth * Factorial( nth - 1 )

def Factorial(nth):
    total = nth
    while nth > 1:
        total *= (nth - 1)
        nth -= 1
    return total


for i in range(1,10):
    print ( Factorial(i) )

