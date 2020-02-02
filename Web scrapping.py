#!/usr/bin/env python
# coding: utf-8

# # Web scrapping

# In[2]:


import urllib


# In[3]:


print(dir(urllib))
help(urllib)


# In[4]:


#request - response
import urllib.request


# In[5]:


print(dir(urllib.request))


# In[7]:


from urllib.request import urlretrieve
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv'

urlretrieve(url, 'forestfiles.csv')


# In[10]:


import pandas as pd
df=pd.read_csv('forestfiles.csv')
df.head()


# In[11]:


from urllib.request import urlopen, Request
url='https://www.wikipedia.org/'
request = Request(url)
response=urlopen(request)

html= response.read()
response.close()  #closing request

print(type(response)) 
print(html)


# In[12]:


import requests    #any website's html file open 
url ='https://www.wikipedia.org/'
r = requests.get(url)
text= r.text #to convert into string format
print(text)


# In[14]:


from bs4 import BeautifulSoup
import requests #used for
url='https://www.crummy.com/software/BeautifulSoup/'
r=requests.get(url) #http response object - get
html_doc = r.text #response to string conversion
soup= BeautifulSoup(html_doc) #convert into BeeautifulSoup Object - Class name with argument string
print(soup.prettify())  #indentations


# In[16]:


print(soup.title) #extracting title only
print(type(soup.title))
soup.title.string #just show text from title tag


# In[17]:


print(soup.get_text()) #extracting all texts - no tags 


# In[19]:


a_tags=soup.find_all('a')
print(a_tags[0:4])

for link in a_tags:
    print(link.get('href'))


# In[ ]:




