# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 13:21:31 2020

@author: ludvi
"""
import sys
import random

# *** INIT - METHODS *** #

#Method, that generates data:
def generateData(outcomeList, k, throws):
    
    #List of results:
    results = []
    
    #Switch, to indicate, whether a switch has been made:
    switch = 0
    
    #Generate data - There are multiple conditions to take into account,
    #which can be seen throughout the following:
    for i in range(0,k):
        dice = 3
        
        #Initiate lists, that check which dices to keep:
        keepList = [] # Normal keep list
        pressureList = [] # Pier pressure list
        
        #Boolean, for choosing dice list:
        pressure = False
        
        for j in range(0,throws):
    
            #Generate throw:
            die = random.choices(outcomeList, k=dice)
            
            
            #Result, with keepList:
            resultsKeep = sum(die) + sum(keepList)
            resultsPressure = sum(die) + sum(pressureList)
                
            #For lower switch:
            if switch % 2 != 0:
                
                if len(results) >= 3 and resultsKeep < min(maxThree(results, len(results))):
                    results.append(resultsKeep)
                    break
                else:
                        
                    #If a switch has occurred:
                    if resultsKeep >= 260:
                        switch += 1
                        results.append(resultsKeep)
                        break
                    elif resultsPressure >= 260:
                        switch += 1
                        results.append(resultsPressure)
                        break
                    
                    #For loop, that chooses which die to keep, due to pier pressure:
                    for p in range(0,len(die)):
                        if die[p] == 100:
                            pressureList.append(die[p])
                        elif die[p] == 60 and not any(elem == 60 for elem in pressureList):
                            pressureList.append(die[p])
                    
                    
                    if len(pressureList) < 2:
                        
                        #Reset pressureList:
                        pressureList = []
                        
                        #For loop, that chooses which die to keep:
                        for l in range(0,len(die)):
                            if die[l] <= 5:
                                keepList.append(die[l])
                    else:
                        pressure = True
                            
                    
            #For normal switch:
            else:
                if len(results) >= 3 and resultsKeep > max(minThree(results, len(results))):
                    results.append(resultsKeep)
                    break
                else:
                    
                    #If a switch has occurred:
                    if resultsKeep == 6 or resultsKeep == 7:
                        switch += 1
                        results.append(resultsKeep)
                        break
                    elif resultsPressure == 6 or resultsPressure == 7:
                        switch += 1
                        results.append(resultsPressure)
                        break
                    
                    #For loop, that chooses which die to keep, due to pier pressure:
                    for p in range(0,len(die)):
                        if die[p] == 2:
                            pressureList.append(die[p])
                        elif die[p] == 3 and not any(elem == 3 for elem in pressureList):
                            pressureList.append(die[p])
                    
                    if len(pressureList) < 2:
                        #Reset pressureList:
                        pressureList = []
                        pressure = False
                        #For loop, that chooses which die to keep:
                        for l in range(0,len(die)):
                            if die[l] >= 60:
                                keepList.append(die[l])
                    else:
                        pressure = True
                        
            #If there is reasonable claim for being pier pressured:
            if pressure:
                dice = 3 - len(pressureList)
            
            #Else, throw out what you would normally throw out:
            else:
                dice = 3 - len(keepList)
            
            #Gather result:
            if j == (throws - 1):
                if pressure:
                    results.append(resultsPressure)
                else:
                    results.append(resultsKeep)
    return results

#Method, that returns the three largest elements of a list:
def maxThree(arr, arr_size):
    
    if arr_size < 3:
        raise Exception("Array size is not sufficient")
    
    third = second = first = -sys.maxsize
    
    for i in range(0,arr_size):
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]
        
        elif arr[i] > second:
            third = second
            second = arr[i]
            
        elif arr[i] > third:
            third = arr[i]
        return [first, second, third]

#Method, that returns the three smallest elements of a list:
def minThree(arr, arr_size):
    
    if arr_size < 3:
        raise Exception("Array size is not sufficient")
    
    third = second = first = sys.maxsize
    
    for i in range(0,arr_size):
        if arr[i] < first:
            third = second
            second = first
            first = arr[i]
        
        elif arr[i] < second:
            third = second
            second = arr[i]
            
        elif arr[i] < third:
            third = arr[i]
        return [first, second, third]

# *** INIT - METHODS *** #