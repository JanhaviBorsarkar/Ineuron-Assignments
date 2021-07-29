#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Q1. Write a Python Program to Check if a Number is Positive, Negative or Zero
n = int(input("Enter a number: "))
if n < 0:
    print("The number is negative")
elif n == 0:
    print("The number is zero")
else:
    print("The number is positive")


# In[ ]:


# Q2. Write a Python Program to Check if a Number is Odd or Even
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


# In[ ]:


# Q3. Write a Python Program to Check Leap Year
year = int(input("Enter year to check: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year!")
        else:
            print("Not a leap year")
    else:
        print("Leap year!")
else:
    print("Not a leap year")


# In[ ]:


# Q4. Write a Python Program to Check Prime Number
n = int(input("Enter a number: "))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime number")
            break
        else:
            print("Prime number")
            break
else:
    print("Number is less than 1")


# In[ ]:


# Q5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000
for p in range(1, 10001):
    if p > 1:
        for i in range(2, p):
            if p % i == 0:
                break
            else:
                print(i)


# In[ ]:




