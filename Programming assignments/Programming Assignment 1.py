#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q1. Write a Python program to print "Hello Python"
print("Hello Python")


# In[2]:


# Q2. Write a Python program to do arithmetical operations addition and division
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
add = a + b
div = a / b
print("The sum of {0} and {1} is {2}" .format(a, b, add))
print("The division of {0} and {1} is {2}" .format(a, b, div))


# In[3]:


# Q3. Write a Python program to find the area of a triangle
base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("Area of triangle is ",area)


# In[4]:


# Q4. Write a Python program to swap two variables
a = 20
b = 30
print("The numbers beore swapping are: ", a,b)
a,b = b,a
print("The numbers after swapping are: ",a,b)


# In[5]:


# Q5. Write a Python program to generate a random number
import random 
print(random.randint(0,10))


# In[ ]:




