#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:28:04 2019

@author: georginasampson
"""

class Descriptive_Calc:
    def __init__(self,data):
        self.data = data
        self.determine_attributes()
        
    def determine_attributes(self):
        self.length = len(self.data)
        self.total = sum(self.datadata)
        self.mean = self.__Find_mean()
        
    def determine_att(self):
            self.length = len(self.data)
        
    def find_mean(self):
            return self.total/(self.length)
            
    
    def find_median(self):
            self = sorted(self)
            listlenght = len(self)
            