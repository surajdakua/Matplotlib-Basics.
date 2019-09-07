'''
@author Suraj Dakua
Find common elements present in two list.
Consider we have two arrays of elements n in array1 and elements m in array2.
We have two array for simplicity let us consider m <= n.
Time complexity for this problem will be O(m*n) because we are comparing each m elements 
of array1 to n elements of array 2. Mathematically we are doing m*n.
And space complexity is O(1) because we not using any additional space.
Space complexity is the amount of working storage and algorithm needs.
'''

import numpy as np 
array1 = np.arange(1,20)
array2 = np.arange(15,30)

count = 0
for i in array1:
    for j in array2:
        if i == j:
            print(i)
            count += 1

print('Number of common elements in two arrays: ', count)