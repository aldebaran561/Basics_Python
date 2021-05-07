#!/usr/bin/env python
# coding: utf-8

# In[6]:


#If...Else function

def ifelse(num1,num2):
    if num1 < num2:
        print('{} is lower than {}'.format(num1,num2))
    elif num2 > num1:
        print('{} is higher than {}'.format(num1,num2))
    else:
        print('{} and {} are the same number'.format(num1,num2)) 


# In[7]:


ifelse(5,8)
ifelse(10,7)
ifelse(2,2)


# In[8]:


# While loops functions

def whileloop(start,ending):
    while start <= ending:
        print('this is a tutorial')
        start +=1


# In[9]:


whileloop(2,5)


# In[13]:


def whileloop_2(start,ending):
    while start <= ending:
        if start < 0:
            print('Starting number could not be negative')
            break
        else:
            print('This is a tutotrial')
            start +=1


# In[15]:


whileloop_2(-10,5)
whileloop_2(2,7)


# In[17]:


# For loops functions

def forloop(string):
    for i in string:
        print(i)
        
def forloop2(ending, start=0):
    for i in range(start, ending):
        print(i)

def forloopmixed(string):
    for i,j in enumerate(string):
        print(i,j)
    


# In[19]:


forloop('Alfa')


# In[20]:


forloop2(10,3)


# In[21]:


forloop2(5)


# In[22]:


forloopmixed('Alfa is a cat')


# In[ ]:




