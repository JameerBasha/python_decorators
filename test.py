#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 12:16:43 2019

@author: jameerbasha
"""
from functools import wraps

def decorator_function(original_function):
    @wraps(original_function)
    def wrapper_function(*args,**kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function

class decorator_class(object):
    def __init__(self,original_function):
        self.original_function=original_function
    def __call__(self,*args,**kwargs):
        print('call executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args,**kwargs)

@decorator_class
@decorator_function
def display():
    print('display function ran')

@decorator_class
@decorator_function
def display_info(name,age):
    print('display info ran with arguments ({},{})'.format(name,age))


display()

display_info('John',25)