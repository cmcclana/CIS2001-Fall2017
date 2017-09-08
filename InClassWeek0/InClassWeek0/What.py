from Base import *
from Treble import *

class What(Base, Treble):
    """description of class"""

    def get(self):
        return Base.get(self) + Treble.get(self) + " What?"


