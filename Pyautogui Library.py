#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyautogui as pg


# In[7]:


pg.position()


# In[9]:


pg.moveTo(352,310,4)   #x y coordinates and timestamp #mouse automation


# In[10]:


pg.click(780,17)  #move and click


# In[11]:


pg.moveTo(500,7,4)
pg.click()


# In[13]:


pg.position()


# In[18]:


pg.moveTo(948,11,4)
pg.click()
pg.moveTo(461, 422, 4)
pg.click()

pg.write('Hello\n', interval=0.25) #write hello in search bar - \n to enter


# In[21]:


pg.hotkey('winleft', 'left') #minimize or maximize windows


# In[20]:


pg.size() #screen size


# In[22]:


pg.position()


# In[27]:


pg.moveTo(208,754,4)
pg.click()
pg.write('Calc\n', interval=0.25)
pg.PAUSE=5
pg.press('5')
pg.press('*')
pg.press('3')
pg.press('=')
pg.hotkey('alt4')


# In[ ]:




