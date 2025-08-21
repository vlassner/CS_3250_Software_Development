'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Description: Simple models for OOP Practice
'''

import math 

class Rectangle: 

    DEFAULT_MEASURE = 1

    def __init__(self, width: int = DEFAULT_MEASURE, height: int = DEFAULT_MEASURE):
        self.__width = max(width, Rectangle.DEFAULT_MEASURE)
        self.__height = max(height, Rectangle.DEFAULT_MEASURE)

    @property #getter
    def width(self) -> int: 
        return self.__width
    
    @width.setter 
    def width(self, width: int): 
        if width > 0: 
            self.__width = width

    @property 
    def height(self) -> int: 
        return self.__height
    
    @height.setter 
    def height(self, height: int): 
        if height > 0: 
            self.__height = height

    def area(self) -> float: 
        return self.__width * self.__height
    
    def perimeter(self) -> float:
        return 2 * (self.__width + self.__height)
    
    def diagonal(self) -> float:
        return math.sqrt(self.__width**2 + self.__height**2)
    
    def __str__(self) -> str: 
        return f'({self.__width}, {self.__height})'
    
# TODO use singleton to make sure only 1 instance of rectangle exists
class SingletonRectangle: 

    _instance = None
        
    @staticmethod
    def get_instance(width, height) -> Rectangle: 
        if not SingletonRectangle._instance:
            SingletonRectangle._instance = Rectangle(width=width, height=height)
        return SingletonRectangle._instance
    
class Vehicle: 

    def __init__(self, manufacturer: str, model: str, year: str): 
        self.__manufacturer = manufacturer 
        self.__model = model 
        self.__year = year 

    def __str__(self) -> str: 
        return f'{self.__manufacturer} {self.__model} ({self.__year})'
    
class Car(Vehicle):

    def __init__(self, manufacturer: str, model: str, year: str, type: str): 
        super().__init__(manufacturer, model, year)
        self.__type = type

    def __str__(self) -> str: 
        return f"{super().__str__()} - {self.__type}"
    
class Truck(Vehicle):

    DEFAULT_CLASSIFICATION = 1

    def __init__(self, manufacturer: str, model: str, year: str, classification: int): 
        super().__init__(manufacturer, model, year)
        self.__classification = max(classification, Truck.DEFAULT_CLASSIFICATION)

    def __str__(self) -> str: 
        return f"{super().__str__()} - {self.__classification}"
    
class StackAdapter:

    def __init__(self):
        self.list = []

    def push(self,value):
        self.list.append(value)

    def pop(self):
        if len(self.list) ==0:
            raise Exception("Stack is Empty!")
        value = self.list[-1]
        self.list = self.list[:-1]
        return value