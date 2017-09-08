from Progression import *

class FibonacciProgression(Progression):
    """description of class"""


    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        #self._prev, self._current = self._current, self._prev + self._current
        old_current = self._current
        self._current = old_current + self._prev
        self._prev = old_current