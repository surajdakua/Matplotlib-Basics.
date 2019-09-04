'''
@author Suraj Dakua. 
Numpy IS A PACKAGE FOR MULTI-DIMENSIONAL ARRAY.
Designed for scientific computation.
Numpy is array oriented computing.
Numpy is memory efficient and provides extremely fast numerical computation.
'''
import numpy as np 
'''
Below shown the 1-D array.
1-D array is called a vector
'''
nparr = np.array([100,101,102,103,104])
#length returns the size of the rows in the array
print(len(nparr))
print(nparr.ndim)

'''
convert 1-D array to 2-D array using function newaxis.
'''
nparr1 = nparr[:, np.newaxis]
print(nparr1)

'''
Convert 2-D array to 1-D array using ravel function.
This is also called flattening. 
Similarly we can use rehape function to reshape the matrix.
'''
print(nparr1.ravel())

'''
shape returns the size of the matrix i.e. mxn
remember shape always return a tuple.
'''
print(nparr.shape) 
print(nparr1.shape)  

'''
Below shown the 2-D array.
Note the 2-D array should be list inside list.
2-D array is called as a matrix.
'''

nparr = np.array([[100,101,102,103,104], [107, 202, 233, 124,435]])
print(len(nparr))
print(nparr.ndim)
print(nparr.shape)   

''' 
Below shown the 3-D array.
Note the 3-D array should be list inside list inside list.
Similary we can create N-dimensional array. 
Note the N-dimensional array is called as a TENSOR.
3-D means it has 3 matrices with shape mxn ex: 3x3x2
'''
nparr = np.array([[[1,2,3,4],[5,6,7,8]], [[1,2,3,4],[6,7,8,9]]])
print(len(nparr))
print(nparr.shape)
print(nparr.ndim)

'''
Create np array using stepsize
Start, Stop and Stepsize is the arguments written inside the parenthesis.
'''
nparr = np.arange(1,10,3)
print(nparr)

'''
Numpy array using linspace.
Start Number, Stop Number, Third argument is divide the start stop in parts that we provide.
Lets see the below example.  
'''
nparr = np.linspace(1,2,5) #range 1 to 2 will be divided into 5 parts.
print(nparr)

'''
Print zeros and ones using np.zeros and np.ones 
'''
arr = np.zeros((4,4))
print(arr)
arr = np.ones((4,4))
print(arr)

'''
create identity matrix where the diagonal elements of the matrix are one.
 using np.eye function. 
'''
arr = np.eye(4) #identity matrix of 4 row 4 column.
print(arr)
arr = np.eye(4,2)  #identity matrix of 4 rows and 2 columns.
print(arr)

'''
Print diagonal matrix using np.diag
Note diagonal matrix is a 2-D matrix.
'''
arr = np.diag([1,2,3,4,5])
print(arr) #prints diagonal matrix of 5rows and 5columns with diagonal elements 1,2,3,4,5. 
#to see the diagonal elements of the matrix
print(np.diag(arr))

'''
generate random number usinng np.random.rand() 
rand() gives random number which are uniformly distributed meaning having values between 0 and 1.
'''
arr = np.random.rand(5) 
print(arr)  #print any 5 random numbers.
arr = np.random.randn(4)  #randn - random normal.
print(arr)

'''
assign a custom value to matrix.
'''
arr1 = np.diag([1,2,3])
arr1[2,1] = 10 #assign value 10 to third row first column of matrix arr.
print(arr1)

'''
Slicing the numpy array
'''
arr = np.arange(10)
#start index stop index and step size.
print(arr[0:9:3]) 

'''
Change the value of array 
'''
arr[5:] = 8 #change the value of array from index 5 to the last index.
print(arr)

'''
Reverse a array
'''
a = arr[::-1] #-1 indicates the inde of last element of the array.
print(a)
    
'''
Perform scalar addition and squaring each element of the array.
'''
arr = np.array([1,2,3,4])
print(arr+1) #this is known as scalar addition. Adding 1 to each element fof the numpy array.
print(arr**2) #square each element of the array. Also known as exponent operator.

'''
Perform subtraction, multiplication of two array.
'''
a = np.ones(4) + 1
print(a)
print(a - arr)
print(arr*a)

'''
Matrix-Matrix multiplication
'''
a = np.diag([1,2,3])
b = np.diag([5,6,7])
print(a*b)

'''
Compare element-wise comparison and it returns a boolean.
'''
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
print(a==b)
print(b>a)

'''
Array-wise comparisions using array_equal function.
'''
print(np.array_equal(a,b))

'''
Array using mathematical function sin, log, exponentaion(base of natural log.)
'''
print(np.sin(a))  #returns sin value of elements in a array.
print(np.log(b))  #returns logarithmic values of array.
print(np.exp(a))  #returns exponent values of an array.
print(np.cos(a))  #return cos values of an array.

'''
Find the sum of all the elements in an array.
when axis = 0 it does the column wise sum
when axis = 1/-1 it does the row wise sum
'''
# print(arr.sum(axis=0))
# print(arr.sum(axis=1))

'''
Find the min and max of the array.
'''
print(a.min())
print(b.max())
print(b.argmax())  #argmax return the index of the maximum value of the array.
print(a.argmin())

'''
any,all, median, std, transponse of an array.
'''
print(np.any(a==2))
print(np.all(a==b))
print(np.median(a))
c = np.transpose(arr1)
print(c)


