# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 16:40:20 2022

@author: arumugaraj
"""


#### pattern formation
#n = 5
rows = int(input("input your no of rows:"))
print("number of rows are:", rows)
columns = int(input("input your no of columns:"))
print("number of columns are:", columns)

# ######### ## square pattern

# for i in range(rows): # no.of rows
#     for j in range(columns): # no.of columns
#         print('@', end ="          ") # print @ in a single line and the gap in the end will decide gap in the output *
#     print() # next loop/row starts from new line
    
# ###########################################
    
    
# ########## # increasing triangle pattern
# for i in range(rows): 
#     for j in range(i+1): # i variable changing in each row and +1 make no.of *
#         print('*', end =" ") 
#     print() 
# ###########################################    
    
# ##### # decreasing triangle
# for i in range(rows): 
#     for j in range(i,rows): # (rows-i) i variable changing in each row and +1 make no.of *
#         print('$', end =" ") 
#     print() 
# ###########################################
    
# ###### # Right sided triangle (use increasing space and decreasing triangle *)
# for i in range(rows): # decide total no.rows
#     for j in range(i,rows): # decreasing triangel with empty space
#         print(" ", end=" ")
#     for j in range(i+1): # increasing triangle with *
#         print("*", end=" ") # Note: end space for both loop should be same
#     print()
    
#  ###########################################
   
##### # # Left sided triangle (use decreasing space and decreasing triangle *)
# for i in range(rows): # decide total no.rows
#     for j in range(i+1): # decreasing triangel with empty space
#         print(" ", end=" ")
#     for j in range(i,rows): # increasing triangle with *
#         print("*", end=" ") # Note: end space for both loop should be same
#     print()
# ###########################################


##### # # Hill mountain pattern (increasing space + increasing * + increasing *)
# for i in range(rows): 
#     for j in range(i,rows): 
#         print(" ", end=" ")
#     for j in range(i):  # To get peak * print one less column in the nested loop
#         print("*", end=" ") 
#     for j in range(i+1):
#         print("*", end = " ")
#     print()
    
# ###########################################
##### # Reverse mountain (incrasing space + decrasing * + increasing *)
    
# for i in range(rows): 
#     for j in range(i+1): 
#         print(" ", end=" ")
#     for j in range(i,rows-1): # To get peak * print one less column
#         print("*", end=" ") 
#     for j in range(i,rows):
#         print("*", end = " ")
#     print()
###########################################
   
##### Diamond pattern (add hill mountain + Reverse hill mountain)

# for i in range(rows-1): # To make single centre line pattern reduce 1 row
#     for j in range(i,rows): 
#         print(" ", end=" ")
#     for j in range(i):  # To get peak * print one less column in the nested loop
#         print("*", end=" ") 
#     for j in range(i+1):
#         print("*", end = " ")
#     print()
    
    
# for i in range(rows): 
#     for j in range(i+1): 
#         print(" ", end=" ")
#     for j in range(i,rows-1): # To get peak * print one less column
#         print("*", end=" ") 
#     for j in range(i,rows):
#         print("*", end = " ")
#     print()
    
# ###########################################



# Number pattern (pattern + number)
"""   Note here first form the pattern by using above method and then try to print numbers 
instead of * and don't touch loop variables, so create a new variable to print the numbers """ 

# increasing triangle pattern

# p =1
# for i in range(rows):
#     for j in range(i+1):
#         print(p, end=" ") # To print same values in the pattern only use this line
        
#     p+=1 # To print different numbers in different rows   
#     print()
    
    
# decreasing triangle pattern

# p =rows
# for i in range(rows):
#     for j in range(i, rows):
#         print(p, end=" ") # To print same values in the pattern only use this line
        
#     p-=1 # To print different numbers in different rows   
#     print()
    
#### similarly we can create different patterns with increasing row values

### To print different numbers in odd and even rows in increasing triangle
# p =0
# for i in range(rows):
#     for j in range(i+1):
#         print(p, end=" ") # To print same values in the pattern only use this line
        
#     p+= 2# To print different numbers in different rows   
#     print()
    
    
    
#### To print alternate diferent numbers in even and odd rows
# for i in range(rows):
    
#     for j in range(i+1):
#         if (i%2==0):
#             print("1", end=" ") # To print same values in the pattern only use this line
            
#         else:
#             print("2", end=" ")
        
#     print()


### To print diamond pattern for numbers
# p = 1
# for i in range(rows-1): # To make single centre line pattern reduce 1 row
#     for j in range(i,rows): 
#         print(" ", end=" ")
#     for j in range(i):  # To get peak * print one less column in the nested loop
#         print(p, end=" ") 
#     for j in range(i+1):
#         print(p, end = " ")
#     p+=1
#     print()
    
    
# for i in range(rows): 
#     for j in range(i+1): 
#         print(" ", end=" ")
#     for j in range(i,rows-1): # To get peak * print one less column
#         print(p, end=" ") 
#     for j in range(i,rows):
#         print(p, end = " ")
#     p-=1
#     print()
    
    
    
#### maintain same numbers in rows and change column numbers
# for i in range(rows): # To make single centre line pattern reduce 1 row
#     p= 1
#     for j in range(rows+1): 
#         print(" ", end=" ")

#     for j in range(i+1):
#         print(p, end = " ")
#         p+=1
#     print()



""" To print pattern of characters ASCII A-Z (65-90), a-z(97-122), 0-9(48-57)"""



p =65
for i in range(rows):
    for j in range(i+1):
        print(chr(p), end=" ") # To print same values in the pattern only use this line
    p+=1 # To print different numbers in different rows   
    print()
    



