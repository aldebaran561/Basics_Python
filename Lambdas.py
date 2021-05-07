#!/usr/bin/env python
# coding: utf-8

# In[14]:


triple = lambda x : x * 3
print(triple(4))

def double(lista):
    return list(map(lambda x : x * 2, lista))

def pares(lista):
    return list(filter(lambda x : (x%2 == 0), lista))
    


# In[15]:


lista = [2,4,5,6]

pares(lista)


# In[ ]:




