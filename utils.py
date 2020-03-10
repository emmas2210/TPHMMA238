# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
from matplotlib import pyplot 
import numpy as np
M = np.zeros((100,100))
M[3,3] = M[4,4] = M[3,4] = M[4,3] = 1
N = np.zeros((100,100))
N[3,3]= N[4,2]=N[4,4]=N[5,3]=1
O=np.zeros((100,100))
O[3,3]=O[3,4]=O[4,3]=O[5,4]=O[4,5]=1

