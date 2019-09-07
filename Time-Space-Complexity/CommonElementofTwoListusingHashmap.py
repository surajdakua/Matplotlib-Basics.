'''
@author Suraj Dakua
Find common elements of two list using Hashtable Dictionary
Note Dictionary of Python is same as Hashtable in Java.
The most important property of dict or hastable is when you write d.get[key]
it finds the exact row in the table instead of traversing throught the whole table means
it does in O(1) which saves a lot of computation time.
Using a dict or Hashtable save the time as well as space.
'''
import numpy as np 
import random

#two arrays using numpy
array1 = np.arange(1,20)
array2 = np.arange(15,30)

#shuffle the array using random function.
random.shuffle(array1)
random.shuffle(array2)

#create a empty dictionary.
Hdict = {}

#add all elements of to the hastable or dictionary
for element in array2:
    # any value is ok. only key is important.
    Hdict[element] = 3    

#now find the common elements in two list.
count = 0
for i in array1:
    if Hdict.get(i) != None:
        print(i)
        count += 1

print('The common numbers in two lsit: ', count) 

