from Stack import *
from Queue import *

def braces_are_matching(text):
    braces = Stack()
    
    open_braces = [ '(', '[', '{' ]
    closed_braces = [ ')', ']', '}' ]
    
    for char in text:
        if char in open_braces:
            braces.push(char)
        elif char in closed_braces:
            if braces.is_empty():
                return False
            
            open_brace = braces.peek()
            if open_brace == '(' and char != ')':
                return False
            elif open_brace == '[' and char != ']':
                return False
            elif open_brace == '{' and char != '}':
                return False
            else:
                braces.pop()
    
    return braces.is_empty()



def reverse_string(text):
    if len(text) == 1:
        return text
    return text[len(text) - 1] + reverse_string(text[0:len(text) -1 ])

def reverse_string_with_stack(text):
    stack = Stack()
    for char in text:
        stack.push(char)
    result = ""
    while not stack.is_empty():
        result += stack.pop()
    return result


print( reverse_string("Eric") )
print( reverse_string_with_stack("Eric") )