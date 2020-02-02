#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pyautogui as pg


# In[4]:


pg.alert(text='', title='', button='OK')


# In[5]:


pg.alert('Your coding file','alert box', button='abc')


# In[8]:


btn=pg.confirm(text='hey',title='s',buttons=['OK','Cancel'])
if btn == 'OK':
    print("You selected to delete file")
    print('Hey')
else:
    print('ooops')


# In[11]:


pw=pg.prompt(text='d', title='e', default='w')
if pw == 'OK':
    print('jey')
else:
    print('Ops')


# In[ ]:


pg.password()

