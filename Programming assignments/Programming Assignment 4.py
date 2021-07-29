#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Q1.	Write a Python Program to Find the Factorial of a Number
n = int(input("Enter a number: "))
fact = 1
if n < 0:
    print("Please enter a positive integer")
elif n == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, n + 1):
        fact = fact * i
    print("Factorial of {0} is {1}" .format(n , fact)) 


# In[3]:


# Q2.	Write a Python Program to Display the multiplication Table
n = int(input("Enter a number: "))
for i in range(1,11):
    print(n * i)


# In[4]:


# Q3.	Write a Python Program to Print the Fibonacci sequence
n = int(input("How many numbers? "))
n1, n2 = 0, 1
count = 0
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1


# In[5]:


# Q4.	Write a Python Program to Check Armstrong Number
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# In[6]:


# Q5.	Write a Python Program to Find Armstrong Number in an Interval
lower = 100
upper = 2000
for num in range(lower, upper + 1):
   order = len(str(num))
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
   if num == sum:
       print(num)


# In[7]:


# Q6.	Write a Python Program to Find the Sum of Natural Numbers
num = int(input("Enter a number: "))
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)


# In[ ]:




