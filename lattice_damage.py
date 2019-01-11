'''
Created on Dec 30, 2018

@author: wange
'''
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import scipy.interpolate as itp


def inidis(depth):
    ins=np.ones(depth)
    surs=np.insert(ins,0,10)
    return surs

def damage(distrib):
    return

def ion_energy_num():
    return    
    
    
if __name__ == '__main__':
    depth=10
    inidistrib=inidis(depth)
    enddistrib=damage(inidistrib)
    print(inidistrib)