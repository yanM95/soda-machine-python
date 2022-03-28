# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 14:34:15 2022

@author: ygm
"""

class Singleton_base(object):
    
    _instance = None
    
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance
