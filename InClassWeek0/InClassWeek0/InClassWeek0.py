from Polygon import *
from Rectangle import *
from Square import *
from Treble import *
from Base import *
from What import *

from Progression import *
from ArithmeticProgression import *
from FibonacciProgression import *

print('hello world!')

rectangle = Rectangle('rectangle', 4, 10, 20)
print( rectangle.get_name() )
print( rectangle.get_area() )
print( rectangle.get_perimeter() )
print( rectangle )

square = Square("square", 4, 2)
print( square )

base = Base()
print(base.get())

treble = Treble()
print( treble.get())

what = What()
print( what.get())

progression = Progression()
progression.print_progression(10)

arithmeticProgression = ArithmeticProgression(2)
arithmeticProgression.print_progression(10)

fib = FibonacciProgression()
fib.print_progression(10)