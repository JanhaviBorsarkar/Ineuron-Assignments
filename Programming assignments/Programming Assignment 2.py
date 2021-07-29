#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q1. Write a Python program to convert kilometers to miles
km = int(input("Enter number of kilometes: "))
miles = km * 0.621371
print("{0} kilometers is {1} miles" .format(km, miles))


# In[2]:


# Q2. Write a Python program to convert Celsius to Fahrenheit
# (0°C × 9/5) + 32 = 32°F
c = int(input("Enter the temperature in celcius: "))
f = (c * 9/5) + 32
print("{0} degree Celsius is {1} Fahrenheit" .format(c, f))


# In[4]:


# Q3. Write a Python program to display calendar
import calendar  
yy = int(input("Enter year: "))  
mm = int(input("Enter month: "))  
print(calendar.month(yy,mm))  


# In[5]:


# Q4. Write a Python program to solve quadratic equation
import cmath
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

d = (b ** 2) - (4 * a * c)
solution1 = (-b - cmath.sqrt(d)) / (2 * a)
solution2 = (-b + cmath.sqrt(d)) / (2 * a)
print("The solution of the quadratic equation is: ", solution1, solution2)


# In[6]:


# Q5. Write a Python program to swap two variables without temp variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("The original numbers are: ",a,b)
a, b = b, a
print("The numbers after swapping are: ",a ,b)


# In[ ]:




