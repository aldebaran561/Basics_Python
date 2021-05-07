#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Here are some examples of fuctions created in Python

def salute():
    print('Hello World')
    
def contador(start, ending):
    for i in range(start,ending):
        print(i)

def saludo_personal(name):
    print('Hola {}'.format(name))

def outer_function():
    print("Hello I'm outer function")
    def innerFunction():
        print("Im inner function")
    innerFunction()

