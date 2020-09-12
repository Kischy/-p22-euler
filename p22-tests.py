# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 12:20:22 2020

@author: kisch
"""

import unittest
from name_value import NameValue as NV


class TestSomething(unittest.TestCase):  
    
    def test_word_value(self):  
        nv = NV()
        
        self.assertEqual(nv.word_value("COLIN"),53)


        
    def test_letter_value(self):  
        nv = NV()
        
        self.assertEqual(nv.__letter_value__("A"),1)
        self.assertEqual(nv.__letter_value__("C"),3)
        self.assertEqual(nv.__letter_value__("O"),15)
        
        



if __name__ == '__main__':
    unittest.main(verbosity=0)
