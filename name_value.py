# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 15:55:44 2020

@author: kisch
"""

class NameValue():
    
    def word_value(self,word):
        sum_letters = 0
        
        for letter in word:
            sum_letters += self.__letter_value__(letter)
            
            
        return sum_letters
        
    
    def __letter_value__(self,letter):    
        
        return ord(letter) - 64
    

