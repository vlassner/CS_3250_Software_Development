'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Description: The Thermostat class
'''

import random 

class Thermostat: 

    MIN_SET_POINT = 60
    MAX_SET_POINT = 90
    current_temperature = random.randint(0, 100)

    def __init__(self, set_point = MIN_SET_POINT): 
        if set_point > Thermostat.MAX_SET_POINT: 
            self.__set_point = Thermostat.MAX_SET_POINT 
        elif set_point < Thermostat.MIN_SET_POINT: 
            self.__set_point = Thermostat.MIN_SET_POINT 
        else:
            self.__set_point = set_point
        
    @property 
    def set_point(self) -> int: 
        return self.__set_point
    
    def check_temperature(self) -> None: 
        if Thermostat.current_temperature < self.__set_point: 
            Thermostat.current_temperature += 1 
        elif Thermostat.current_temperature > self.__set_point:
            Thermostat.current_temperature -= 1 
    
    def __str__(self) -> str:
        return f'Set Point: {self.__set_point}F'
