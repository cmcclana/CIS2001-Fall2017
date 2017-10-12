#Write a function FizzyBizzy( n ) that will loop through from 0 to N, putting numbers divisible by 5 in a queue, numbers divisible by 3 in a stack and printing the others.
#Then gets the values out of the queue and prints them.
#Then gets the values out of the stack and prints them

from Stack import Stack
from Queue import Queue

def FizzyBizzy(n):
    stack = Stack()
    queue = Queue()

    for number in range(0, n +1 ):
        if number % 5 == 0:
            queue.enqueue(number)
        if number % 3 == 0:
            stack.push(number)
        if number % 5 != 0 and number % 3 != 0:
            print(number)


    while ( not queue.is_empty() ):
        print( queue.dequeue() )
    while ( not stack.is_empty() ):
        print( stack.pop() )


FizzyBizzy(100)