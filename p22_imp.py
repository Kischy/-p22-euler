# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 15:50:55 2020

@author: kisch
"""

import numpy as np


def import_names_sorted():
    names = np.loadtxt("p022_names.txt",dtype=str,delimiter=",")

    for i in range(len(names)):
        names[i] = names[i][1:-1]
        
    names = np.sort(names)
        
    return names
    