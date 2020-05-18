#!/usr/bin/env python
# coding: utf-8

# In[1]:


# write a program to get a user input in the form of a list data type.Return a list by removing all the duplicates

lst = [] 
  
n = int(input("Enter number of elements : ")) 
  
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele)  
      
print(lst) 

temp = []

for x in lst:
    if x not in temp:
        temp.append(x)

lst = temp

print(f'Updated List after removing duplicates = {temp}')


# In[2]:


# write a program to create a user defined tuple with 'int' data type and perform the following operations

# find the length of tuples
# find the sum of all the elements of a tuple
# find the largest and smallest elements of a tuple

lst = []
  
n = int(input("Enter number of elements : "))
  
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele)
      
print(lst) 

lst = tuple(lst)

print(lst)

print(len(lst))

print(sum(lst))

print(min(lst))

print(max(lst))


# In[8]:


# given a number and ith bit,change th ith of that number to 1

n=13
k=1
if ((1 << k) | n): 
    print("Kth bit set number = ", setKthBit(n, k)) 


# In[9]:


# given a number ,print 1 if the number is odd otherwise print 0

a = [0, 1] 
print ("Enter the number") 
no = input() 
print (a[int(no) % 2])


# In[10]:


# given two lists of integer A and B. Write a program to merge them into a single sorted list that contains every item from list A and B in ascending order

A=[4,5,3,7,8]
B=[6,9,2,10,1]
A.extend(B)
A.sort()
print((A))


# In[28]:


# create a user defined dictionary to store names and marks of 5 students .Sort the dictionary according to marks and return this sorted dictionary to the user

a={}
n=int(input("Number of Elements:"))

for i in range(n):
    k=input("Enter name:")
    v=input("Enter marks:")
    a.update({k:v})

print(a)       
print(sorted(a.items(), key = lambda kv:(kv[1], kv[0])))  
    


# In[ ]:





# In[ ]:




