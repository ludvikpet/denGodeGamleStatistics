# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 13:06:27 2020

@author: ludvi
"""

#Libraries:
import numpy as np
import pandas as pd
import os
import csv
import seaborn as sn
import matplotlib.pyplot as plt
import random
import sys
from init_denGodeGamle import minThree, maxThree, generateData

#Possible outcomes:
outcomeList = [100,2,3,4,5,60]

#Amount of participants:
k = 10

#Amount of throws:
throws = 3

#Generate data:
results = generateData(outcomeList, k, throws)