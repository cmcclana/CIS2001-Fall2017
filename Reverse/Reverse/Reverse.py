import sys

def reverse_list_recursive(list):
    _reverse_list_recursive(list, 0, len(list) - 1)

def _reverse_list_recursive(list, begin, end):
    if begin < end:
        temp = list[begin]
        list[begin] = list[end]
        list[end] = temp
        _reverse_list_recursive(list, begin+1, end-1)

def reverse_list_iter(list):
    begin = 0
    end = len(list) -1
    while begin < end:
        temp = list[begin]
        list[begin] = list[end]
        list[end] = temp


class Binary():
    def __init__(self, number):
        self.number = number
        self._queue = []
        self._stack = []

        # que queue queueue queueueueue
        power = 0
        while 2**power <= number:
            power += 1
        # 2**power is greater than the number, need to reduce the power by 1
        power -= 1

        value = number

        while power >= 0:
            if value >= 2**power:
                #pretending a list is a queue and adding to the back
                self._queue.append(1)
                value -= 2**power
            else:
                #pretending a list is a queue and adding to the back
                self._queue.append(0)
            
            power -= 1

        #stack stacky stacky stack stack
        stack_value = number

        while stack_value > 0:
            if stack_value % 2 == 0:
                # pretending a list is a stack and pushing to the 'top'
                self._stack.insert(0, 0)
            else:
                # pretending a list is a stack and pushing to the 'top'
                self._stack.insert(0, 1)
            stack_value = stack_value // 2

    def print_stack(self):
        value = ''
        while len(self._stack) > 0:
            # pretending a list is stack and taking off the 'top'
            value += str(self._stack.pop(0))

        return value

    def __str__(self):
        value = ""
        while len(self._queue) > 0:
            value += str(self._queue.pop(0))
        return value
        #return "".join( str(binary) for binary in self._queue )

for n in range(256):
    print(Binary(n).print_stack())
