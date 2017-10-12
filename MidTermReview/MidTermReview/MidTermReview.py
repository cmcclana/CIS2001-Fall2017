#Given a 2d list of integers nums, write a function sum_of_center_values( nums ) that returns the sum of the values of all integers in the center of the 2d list.  Your function must work for all sizes of 2d lists.
#For example - in the 2d list below, 6, 7, 10 and 11 are in the middle.
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16


def sum_of_center_values( nums ):
    sum = 0
    for row_number in range(1, len(nums) - 1 ):
        for col_number in range( 1, len(nums[row_number] ) - 1 ):
            sum += nums[row_number][col_number]
    return sum


nums = [
    [ 0, 1, 2, 3, 4, 5 ],
    [ 10, 20, 30, 40, 50, 60 ],
    [ 10, 9, 8, 7, 6, 5 ],
    [ 12, 14, 16, 18, 20, 22 ],
    [ 1, 1, 1, 1, 1, 1 ],
    [ 0, 0, 0, 0, 0, 0]
    ]

#print ( sum_of_center_values( nums ))





def print_string_backwards( to_reverse ):
    if len(to_reverse) == 1:
        return to_reverse
    return to_reverse[-1:] + print_string_backwards( to_reverse[0:-1] )

#Write a recursive function print_string_backwards( to_reverse ) that outputs to_reverse backwards

def print_string_backwards_not_returning( to_reverse ):
    if len(to_reverse) == 0:
        return
    print( to_reverse[-1:], end="" )
    print_string_backwards_not_returning( to_reverse[0:-1] )

#Write an interative function print_string_backwards( to_reverse ) that outputs to_reverse backwards

def interative_print_string_backwarsd( to_reverse ):
    for index in range(len(to_reverse) -1, -1, -1):
    # index = len(to_reverse) - 1
    # while index >= 0:
        print( to_reverse[index], end="" )
        # index -= 1


print( print_string_backwards( "Hello!" ) )

print_string_backwards_not_returning( "Deliver" )
print()
interative_print_string_backwarsd("Yesterday")
print()


#What is wrong with this simple recursive solution to get a Fibonacci sequence number?
def Fib( n ):
  if n < 0:
     return 0
  elif n <= 2:
     return 1
  else
     return Fib( n - 1) + Fib( n - 2 )




#Explain why print(y) still outputs [10] in the following snippet
x = []
y = x
x.append(10)
x = None
print(y)