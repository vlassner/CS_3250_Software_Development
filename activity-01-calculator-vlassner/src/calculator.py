'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Student: Victoria Lassner
Description: Activity 01 - Calculator
'''
import math

class Calculator: 

    DELTA = 0.0000000001

    @staticmethod
    def add(a, b): 
        return a+b
    
    @staticmethod
    def subtract(a, b): 
        return a-b

    @staticmethod
    def multiply(a, b): 
        return a*b

    @staticmethod
    def divide(a, b): 
        return a/float(b)
