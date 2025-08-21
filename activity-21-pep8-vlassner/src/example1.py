import math 

class Rectangle: 
    DEFAULT_MEASURE = 1

    def __init__(self, width = DEFAULT_MEASURE, height = DEFAULT_MEASURE):
        self._width = width if width > 0 else Rectangle.DEFAULT_MEASURE
        self._height = height if height > 0 else Rectangle.DEFAULT_MEASURE

    def area( self ): 
        return self._width*self._height
    
    def perimeter(self):
        return 2 * (self._width + self._height)
    
    def diagonal(self):
        return math.sqrt(self._width**2 + self._height**2)