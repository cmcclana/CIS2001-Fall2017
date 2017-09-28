def fib(nth):
    previous = 1
    current = 1
    if nth == 1 or nth == 2:
        return current
    currentNth = 2
    while nth > currentNth:
        temp = current
        current = current + previous
        previous = temp
        currentNth += 1

    return current

def fibRecursive(nth):
    if nth == 1 or nth == 2:
        return 1
    return _fibResursive(nth, 3, 1, 1)

def _fibResursive(nth, currentNth, previous, current):
    if nth == currentNth:
        return previous + current
    return _fibResursive(nth, currentNth+1, current, previous+current)

def fibEasyRecursive(nth):
    if nth == 1 or nth == 2:
        return 1
    return fibEasyRecursive(nth-1) + fibEasyRecursive(nth-2)


for i in range(1,100):
    print( fibEasyRecursive(i) )
