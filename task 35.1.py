#!/usr/bin/env python
# coding: utf-8

# # Task 35.1

# In[1]:


import cv2
import numpy as n
import math as m


# In[2]:


#drawing black plane image of size 600*800
a = n.zeros((600,800,3), dtype=n.uint8)


# In[3]:


def s():
    cv2.imshow('Flag of India', a)
    cv2.waitKey()
    cv2.destroyAllWindows()
s()


# In[4]:


# changing the image background to white
a[0:,0:] = [255,255,255]
s()


# In[5]:


def show():
    cv2.imshow('Flag of India', flag)
    cv2.waitKey()
    cv2.destroyAllWindows()


# In[6]:


# drawing rectangle for tricolor
flag = cv2.rectangle(a,(197,118),(463,292),[0,0,0],2)
show()

# pole of flag
flag = cv2.line(a, (463,118), (463,500),[0,0,0], 5 )
show()

# chakra of flag
flag = cv2.circle(a,(330,205), 25 , [128,0,0], 2)
show()


# In[7]:


# coloring the flag
a[120:180,200:460] = [0,140,255]
show()

#a[180:230,200:460] = [0,140,255]
a[230:290,200:460] = [0,255,0]
show()


# In[8]:


# drawing 24 chakra line of flag
for i in range(24):
    #i = i * 1
    x1 = 330
    y1 = 205
    angle = i * 15
    θ = angle * (3.14 / 180)
    length = 25
    x2 = x1 + int(length * m.cos(θ))
    y2 = y1 + int(length * m.sin(θ))

    flag = cv2.line(a, (x1,y1),(x2,y2),[128,0,0], 1)


# In[9]:


show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




