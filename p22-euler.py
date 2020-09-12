# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 12:20:22 2020

@author: kisch
"""

from p22_imp import import_names_sorted
from name_value import NameValue as NV



problem_number = 22


print("Calculation started")
names = import_names_sorted()

nv = NV()

the_answer = 0
ind = 1

for name in names:
    the_answer += ind * nv.word_value(name)
    
    ind += 1
    


print("The answer to the " + str(problem_number) + "th problem of ProjectEuler.Net is:",the_answer)


