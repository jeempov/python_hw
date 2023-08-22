'''
1) Has a function to calculate the square footage of a house
Reminder of Formula: Length X Width == Area

2) Has a function to calculate the circumference of a circle

Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage
'''
import math

def house_area(length, width):
    """calculate's a house's square footage if given length and width"""
    area = length * width
    return area 

def circumference(radius):
    """calculates a circle's circumference if given a radius"""
    circumference = 2 * math.pi * radius
    return circumference

