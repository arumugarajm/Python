# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 02:50:03 2022

@author: arumugaraj
"""

from array import*

import numpy as np

###### NOTE: np.array() created ndarray array() create array so always check datatype if any operation fails


arr = array("i", [1,2,3,4]) #here i represents signed integers data i.e, Type codes
print(arr.buffer_info()) # To print memory address and the length of the buffer
print(arr[3]) # To print index value of an array

## To print each elements present in the array
for i in arr:
    print(i)
##################################
#### To print array index with values    
for i in range(len(arr)):
    print(i, arr[i])
    
######################################    
arr.append(10) #append value 10 at the last index
arr.remove(10) #remove specified value from the array
arr.reverse() #reverse the array elements
arr.pop(3)  #	Removes the element at the specified position
arr.insert(3,3) ##	Adds an element at the specified position

b = np.sort(arr) #sort is not there in array so use numpy
b = np.copy(arr) # for copy alsoe use numpy

ind = arr.index(3) ##Returns the index of the first element with the specified value
c = arr.count(3) ##Returns the number of elements with the specified value i,e, how many time a specified values are present in the array

b = array("i", [3,4])
arr.extend(b)  ## Add the elements of a list (or any iterable), to the end of the current list

print(type(arr)) 

#########################################################

### create array using manual input

a = array("i", []) # craeates an empty array
x = int(input("Enter size of the array:")) # type how many elements we want to create an array
print("enter %d elements" %x) # just say how many elements we want to enter

for i in range(x):
    n = int(input())
    a.append(n)
    
    
print(a)

#################################################
b = np.array([]) # craeates an empty array
x = int(input("Enter size of the array:")) # type how many elements we want to create an array
print("enter %d elements" %x) # just say how many elements we want to enter

for i in range(x):
    n = int(input())
    b = np.append(b,n) ## see the differnence here how to append elements
    
    
print(b)

#################################################

########manual creation of 2D array


b = np.array([[],[]]) # craeates an empty array
x = int(input("Enter size of the roes:")) # type how many elements we want to create an array
print("enter %d elements" %x) # just say how many elements we want to enter
y = int(input("Enter size of the columns:")) # type how many elements we want to create an array
print("enter %d elements" %y) # just say how many elements we want to enter

for i in range(x):
    for j in range(y):
        n = int(input())
        p = int(input())
        b[i,j] = np.append(b[i,j],n,p) ## see the differnence here how to append elements
    
    
print(b)

###########################################################################
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
  
# Initialize matrix
matrix = []
print("Enter the entries rowwise:")
  
# For user input
for i in range(R):          # A for loop for row entries
    a =[]
    for j in range(C):      # A for loop for column entries
          a.append(int(input()))
    matrix.append(a)
  
# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print() 
    
    #########one-liner logic to take input for rows and columns
mat = [[int(input()) for x in range (C)] for y in range(R)]
print(mat)


#############################################################################
## create list of list with key value pair
lst = [ ]
n = int(input("Enter number of elements : "))
  
for i in range(0, n):
    ele = [input(), int(input())]
    lst.append(ele)
      
print(lst)
###############################################################
#####To create 2D string array use the same 2D array just remove int
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
  
# Initialize matrix
matrix = []
print("Enter the entries rowwise:")
  
# For user input
for i in range(R):          # A for loop for row entries
    a =[]
    for j in range(C):      # A for loop for column entries
          a.append((input()))
    matrix.append(a)
# ###############################################################################
#######3D array
W = int(input("Enter the number of depths:"))
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

  
# Initialize matrix
f= []
print("Enter the entries rowwise:")
  
# For user input
for k in range(W):
    matrix = []
    for i in range(R):          # A for loop for row entries
        a =[]
        for j in range(C):      # A for loop for column entries
              a.append(int(input()))
        matrix.append(a)
    f.append(matrix)
    
    

        
         