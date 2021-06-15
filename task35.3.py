#!/usr/bin/env python
# coding: utf-8

# # Task 35.3

# In[1]:


import cv2
import numpy as n

#uploading images to read
v = cv2.imread('vk.jpg')
ab = cv2.imread('abd.jpg')


# In[2]:


v.shape


# In[3]:


ab.shape


# In[4]:


collage = n.zeros(( 600, v.shape[1] + ab.shape[1],3), dtype=n.uint8)


# In[5]:


def img():
    cv2.imshow('AB de',collage)
    cv2.waitKey()
    cv2.destroyAllWindows()
img()


# In[6]:


collage.shape


# In[7]:


v = cv2.resize(v[:],(v.shape[1],600)) 
ab = cv2.resize(ab[:],(ab.shape[1],600)) 


# In[8]:


v.shape


# In[9]:


ab.shape


# In[10]:


collage[:,0:v.shape[1]] = v
collage[:,v.shape[1]:] = ab


# In[11]:


img()


# In[ ]:




