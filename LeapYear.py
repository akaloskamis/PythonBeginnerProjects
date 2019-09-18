# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 17:25:32 2019

@author: user
"""

def leap_year(year):
    if year % 400==0 or (year % 4 == 0 and year % 100 !=0):
        return '{} is a leap year'.format(year)
    else:
        return '{} is not a leap year'.format(year)
    
print (leap_year(2019))
print (leap_year(2000))
