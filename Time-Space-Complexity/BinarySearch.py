'''
@author Suraj Dakua
Binary Search Algorithm.
To perform binary search list needs to be sorted.
Steps for Binary Search:
    1. Create a sorted list or array of n numbers.
    2. Compute or find the middle element of the list. 
    3. After first comparison break the array or list and find whether the element lie on the left side or right side of the middle element.
    4. After the first comparison we have n/2 elements.
    5. Next comparison we will have n/4 elements next n/8 and so on after some point it will reach one value only.
Here we will have logarithmic comparisons. In binary search comparisons in the worst case comparison is log(n) of base 2.
Note again all of the above will work if and only if the list is sorted. 
'''
import math
import numpy as np 

def binarysearch(arr,l,r,q):
    if r >= l:
        middle = l + math.floor((r-l) / 2)
        if arr[middle] == q:
            return middle
# if value is smaller than mid value then value is on the
# left part of the array
        elif arr[middle] > q:
            return binarysearch(arr, l, middle-1, q)
# if value is greater than mid value then value is on the
# right part of the array
        else:
            return binarysearch(arr,middle + 1, r, q)
    else:
        return -1

#numpy array of of range 1-20
arr = np.arange(1,21)
print(arr)
q = 16  #value to be searched in the array.

#call the above function and return the index where the value is present.
result = binarysearch(arr,0,len(arr)-1,q)
if result != -1:
    print ("The value is present at indeq %d" %result)
else:
    print ("The value is not present in array.")