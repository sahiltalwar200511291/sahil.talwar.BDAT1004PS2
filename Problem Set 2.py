#!/usr/bin/env python
# coding: utf-8

# # Problem set 2
# ### Sahil Talwar 200511291

# Question 2   
# Function fileLength(), given to you, takes the name of a file as input and returns the length of the file:  
# As shown, if the file cannot be found by the interpreter or if it cannot be read as a text file, an exception will be raised. Modify function fileLength() so that a friendly message is printed instead:

# In[1]:


def fileLength(filename):
   # returns the number of lines in file
    infile = open(filename, 'r')
    lineList = infile.readlines()
    infile.close()
    return len(lineList)

fileLength('example.txt')


# Question 5 Write a recursive method binary() that takes a non-negative integer n and prints the binary representation of integer n.

# In[2]:


def binary(n):
    a=[]
    if n < 0:
        print("NonNegative number is not allowed")
    elif n < 2:
        print(n)
    else:
        while n>0:
            x = n%2
            a.append(x)
            n =n//2
        a.reverse()
    for i in a:
        print(i,end='')
    print(end='\n')
        
binary(0)
binary(1)
binary(3)
binary(9)


# Question No: 8
# Write SQL queries on the below database table that return:  
# a) All the temperature data.  
# b) All the cities, but without repetition.   
# c) All the records for India.  
# d) All the Fall records.  
# e) The city, country, and season for which the average rainfall is between 200 and 400 millimeters.  
# f) The city and country for which the average Fall temperature is above 20 degrees, in increasing temperature order.  
# g) The total annual rainfall for Cairo.  
# h) The total rainfall for each season.  

# In[ ]:




