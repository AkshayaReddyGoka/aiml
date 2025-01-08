#!/usr/bin/env python
# coding: utf-8

# In[2]:


num = 6
if num %2 == 0:
    print("even")
else:
    print("odd")


# In[3]:


num = 0
result = "Positive" if num > 0 else ("Negative" if num < 0 else "zero")
print(result)


# In[4]:


# print even numbers
L =[1,9,2,10,56,89]
[x for x in L if x%2 == 0]


# In[5]:


# print odd numbers
L =[1,9,2,10,56,89]
[x for x in L if x%3 == 0]


# In[6]:


# To print an  average value of the list
L =[1,9,2,10,56,89]
sum([x for x in L])/len(L)


# In[7]:


#dictionary comprehension
d1 = {'Ram':[23,56,87,58], 'jhon':56,46,86,94)}


# In[ ]:




