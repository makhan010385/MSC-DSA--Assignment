#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT - 1

# ## Ques - 1 :- Write a Python program to get the 4th element and 4th element from last of a tuple form below tuple.

# In[20]:


Given_Tuple = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")           #Tuple is Given and is represented by circular brackets


# ### When we start from 0 index then the output is given below:-

# In[21]:


print("4th element : ",Given_Tuple[3])     #Print function will print the output , here in this it print the 4th element of tuple


# In[22]:


print("4th from last element : ",Given_Tuple[6])          #Print function will print the output , here in this it print the 4th element from last of tuple


# ### When we start from negative index then the output is given below:-

# In[23]:


print("4th element : ",Given_Tuple[-7])    #Print function will print the output , here in this it print the 4th element of tuple


# In[24]:


print("4th from last element : ",Given_Tuple[-4])          #Print function will print the output , here in this it print the 4th element from last of tuple


# ## Ques - 2 :- Write a Python program to convert a list to a tuple?

# In[25]:


Given_List = [5, 10, 7, 4, 15, 3]                                           #List is Given and is represented by Square brackets


# ### For converting a List ito Tupple , we simply use Tupple function which is predefined in Python 

# In[26]:


Con_List_To_Tuple = tuple(Given_List)                             #This variable convert List into Tuple Through tupple function
print("After converting : ",Con_List_To_Tuple)             #Print function will print the output of given List to converted Tuple


# ## Ques - 3 :- Write a program to unpack the following tuple into four variables and display each variable.

# ### This code PACKS values into variable Given_Tuple

# In[27]:


Given_Tuple = (10, 20, 30, 40)                                   #Tuple is given and Tuple is immutable i.e. It can't be changed


# ### This code UNPACKS values of variable Given_Tuple

# In[28]:


(a , b , c , d) = Given_Tuple                                  


# In[29]:


print("a : ",a)                                              #Print function will print the output of value of unpack variable a
print("b : ",b)                                              #Print function will print the output of value of unpack variable b
print("c : ",c)                                              #Print function will print the output of value of unpack variable c
print("d : ",d)                                              #Print function will print the output of value of unpack variable d


# ## Ques - 4 :- Write a program to Swap two tuples in Python.

# In[30]:


Given_Tuple1 = (11, 22)                #Tuple is Given and Tuple is a collection which is ordered and unchangable i.e. immutable


# In[31]:


Given_Tuple2 = (99, 88)                #Tuple is Given and Tuple is a collection which is ordered and unchangable i.e. immutable


# ### Before Swapping

# In[32]:


print("Tuple 1 : ",Given_Tuple1)
print("Tuple 2 : ",Given_Tuple2)


# ### After Swapping

# In[33]:


Given_Tuple1 , Given_Tuple2 = Given_Tuple2 , Given_Tuple1                                #This statement will swap the two Tuple
print("Tuple 1 : ",Given_Tuple1)
print("Tuple 2 : ",Given_Tuple2)


# ## Ques - 5 :- Write a program to copy elements 40 and 50 from the following tuple into a new tuple.

# In[34]:


Given_Tuple = (10, 20, 30, 40, 50, 60)         #Tuple is Given and Tuples are used to store multiple items in a single variable.


# ### Firstly finding if there exist 40 and 50 in the given Tuple or not and if present , then we assign it to new Tuple

# In[35]:


if 40 in Given_Tuple and 50 in Given_Tuple:
    New_Tuple = (40 , 50)
print("New_Tuple After Copying = ",New_Tuple)


# ## Ques - 6 :- Write a python program to Counts the number of occurrences of item 50 from a tuple.

# In[36]:


Given_Tuple = (50, 10, 60, 70, 50)             #Tuple is Given and Tuples are used to store multiple items in a single variable.


# ### To find the number of occurence of item 50 in given Tuple , we simply use count function provided by Python

# In[37]:


x = Given_Tuple.count(50)                               #The varialbe is the no. of count which get initialise by count function
print("No. of Occurrence of Item 50 : ",x)

