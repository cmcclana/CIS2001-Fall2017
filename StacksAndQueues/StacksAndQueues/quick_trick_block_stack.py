#Write a method quick_trick_block_stack( n ) that loops through numbers N through 2. If N is prime, create a queue and put it on the stack.  If N is not prime, enqueue N on the top queue.  Return the stack of queues.
#Then loop through the stack of queues printing all the numbers, with each queue on a single line.


from Stack import Stack
from Queue import Queue
import math

def is_prime(n):
    for factor in range(2, int(math.sqrt(n)) + 1 ):
        if n % factor == 0:
            return False
    return True

def quick_trick_block_stack(n):
    stack = Stack()
    queue = Queue()

    stack.push( queue )

    for number in range(n+1, 1, -1):
        if is_prime(number):
            stack.push( Queue() )
        else:
            stack.peek().enqueue( number )

    while not stack.is_empty():
        queue = stack.pop()
        while not queue.is_empty():
            print( queue.dequeue(), end=" ")
        print()


quick_trick_block_stack(100)