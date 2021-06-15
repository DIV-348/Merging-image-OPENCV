#!/usr/bin/env python
# coding: utf-8

# # Task 35.2

# In[1]:


import cv2
import numpy as n


# In[2]:


v = cv2.imread('vk.jpg')
ab = cv2.imread('abd.jpg')


# In[3]:


def images():
    cv2.imshow('AB de',v)
    cv2.imshow('Virat',ab)
    cv2.waitKey()
    cv2.destroyAllWindows()
images()


# In[4]:


model=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

v_face= model.detectMultiScale(v)
ab_face = model.detectMultiScale(ab)


# In[5]:


v_face


# In[6]:


ab_face


# In[7]:


x1=v_face[0][0]
y1=v_face[0][1]
x2=x1 + v_face[0][2]
y2=y1 + v_face[0][3]


xx1=ab_face[0][0]
yy1=ab_face[0][1]
xx2=xx1 + ab_face[0][2]
yy2=yy1 + ab_face[0][3]


# In[8]:


t = n.zeros((v_face[0][2],v_face[0][3], 3), dtype = n.uint8)


# In[9]:


t[0:,0:] = v[y1:y2, x1:x2]
v[y1:y2, x1:x2] = cv2.resize(ab[yy1:yy2,xx1:xx2],(v_face[0][2], v_face[0][3]))
ab[yy1:yy2, xx1:xx2] = cv2.resize(t[0:,0:],(ab_face[0][2], ab_face[0][3]))


# In[10]:


images()


# In[ ]:




