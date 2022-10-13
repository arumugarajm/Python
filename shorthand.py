# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 05:31:27 2022

@author: arumugaraj

"""

""" if condition:
   if-expression
   else:
   else-expression
   
   
 If-expression if(Condition) else else-expression


L = [mapping-expression for element in source-list if filter-expression]  
L       Variable, result gets assigned to

mapping-expression       Expression, which is executed on every loop if only filter-expression in if condition resolved as True
   
   
   """
#### normal for loop
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)
  
# #### using short hand
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# #################################

# ###newlist = [expression for item in iterable if condition == True]
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)


# ###
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

# ###########################
# a = 330
# b = 330

# print("A") if a > b else print("=") if a == b else print("B")
# ############################################

# ############### NOTE: if else with for loop 

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x if x != "banana" else "orange" for x in fruits]

# print(newlist)



######2D
# mat = [[int(input()) for x in range (C)] for y in range(R)]
# print(mat)
   
####3D
d = int(input("Enter number of depths:"))
r = int(input("Enter number of rows:"))
c = int(input("Enter number of columns:"))

#### NOTE: start from right to left means row, column,width
mat = [[[int(input()) for x in range (c)] for y in range(r)]for z in range(d)]
print(mat)





