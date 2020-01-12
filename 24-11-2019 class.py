#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=7
b=7

print(a)
print(b)


# In[2]:


print(id(a))
print(id(b))


# In[3]:


a=7
type(a)


# In[4]:


b=20.7
type(b)


# In[6]:


c= True
type(c)


# In[7]:


d="hello"
type(d)


# In[8]:


#index  0        1       2   3    4
name = ["Ali", "Hamza", 20, True, False]
#index   -5      -4      -3  -2    -1
type(name)
#list


# In[9]:


#index  0        1       2   3    4
name = ("Ali", "Hamza", 20, True, False)
#index   -5      -4      -3  -2    -1
print(name)
print(name[3])
type(name)
#tuple


# In[10]:


name= {"Hamza", "Jumaid", "Kashif", "Hamza"}
print(name)
type(name)


# In[13]:


name= {"Hamza", "Junaid", "Hamza", "Kashif"}
print(name)
print(type(name))
name = list (name)
print(name[2])
type(name)


# In[17]:


data = {"name": "Bushra Khalid",
        "Father_name": "Raja Khalid",
         0:"Pakistan"}
data["name"]


# In[18]:


type(data)


# In[19]:


#get keys
list(data)


# In[21]:


data = {"name": "Bushra Khalid",
        "Father_name": "Raja Khalid",
         0:"Pakistan"}
data["name"]


# In[22]:


data[0]


# # basic operation with String Data Types

# In[28]:


name1 = "BuShrA KhaLiD"
name2 ="bushra khalid"
print(name1==name2)
print(name1, name2, end='\n')


# In[29]:


name1 = "BuShrA KhaLiD"
name2 ="bushra khalid"
print(name1==name2)
print(name1, name2, sep='\n')


# In[30]:


name1 = "BuShrA KhaLiD"
name2 ="bushra khalid"
print(name1==name2)
print(id(name1), id(name2), sep='\n')
#different addresses because different values


# In[31]:


#
help(name1)


# In[32]:


help(str)


# In[33]:


#show methods and attributes that we can use with name1 (or on variable)
dir(name1)


# # methods and attributes on list and strings

# In[34]:


#inline operation
name1="BuShrA KhaLiD"
print(name1.upper())
print(name1)


# In[35]:


#inline operation
name1="BuShrA KhaLiD"
print(name1.lower())
print(name1)


# In[36]:


#in-memory operation
name1="BuShrA KhaLiD"
name1= name1.lower()
print(name1)


# In[37]:


#inline operation
name1="BuShrA KhaLiD"
print(name1.title())
print(name1)


# In[38]:


#delete variable from memory 
del name1
print(name1)


# In[39]:


#inline operation
name1="      BuShrA           KhaLiD             "
print(len(name1))
print(name1.title())


# In[42]:


#inline operation
name1="      BuShrA           KhaLiD             "
print(len(name1))
#left strip - remove extra spaces from left
print(name1.lstrip())
print(len(name1.lstrip()))


# In[43]:


#inline operation
name1="      BuShrA           KhaLiD             "
print(len(name1))
#right strip - remove extra spaces from right
print(name1.rstrip())
print(len(name1.rstrip()))


# In[44]:


#inline operation
name1="      BuShrA           KhaLiD             "
print(len(name1))
#strip - remove extra spaces from left and right
print(name1.strip())
print(len(name1.strip()))


# In[47]:


#Position
a="we are Pakistan we love our country!"
a.find("Pakistan")


# In[48]:


#slicing can be done on list tuple and string - sequence (start, end+1 index, step)
a[7:15:1]


# In[49]:


#Position - if repetition
a="we are Pakistan we love our country!"
a.find("we", 5)


# In[50]:


#Position
a="we are Pakistan we love our country!"
a[a.find("Pakistan"):15]


# In[51]:


#Position
a="we are Pakistan we love our country!"
a[a.find("Pakistan"):25]


# In[52]:


#Position
a="we are Pakistan we love our country!"
b=a.split();
print(b)


# In[53]:


b.count('we')


# In[54]:


b.index("Pakistan") #not inline function


# In[62]:


#NEW LINE
5+7*2 -7 + 2


# In[58]:



card = """
Name: Bushra Khalid
Father Name: Raja Khalid
Program: PIAIC
"""
print(card)


# In[61]:


#concatenation %

names="Bushra"
fname="Khalid"
program = "PIAIC"

print(" Student Name: %s \n Father Name: %s \n Program: %s"%(names, fname, program))


# In[64]:


#concatenation +

names="Bushra"
fname="Khalid"
program = "PIAIC"

" Student Name: " + name + " \n Father Name: " + fname + " \n Program: " + program


# In[71]:


#concatenation in Python 3

names="Bushra"
fname="Khalid"
program = "PIAIC"

print(f' Student Name: {names} \n Father name: {fname}  \n Program: {program}')


# In[72]:


int ("1")+1  #concat


# In[73]:


a = 200
"Pakistan Score: " + str(a) #data type conversion


# In[74]:


#concatenation in Python 3

names="Bushra"
fname="Khalid"
program = "PIAIC"
score= 200

print(f' Student Name: {names} \n Father name: {fname}  \n Program: {program} \n Score: {score}')


# In[75]:


"Name: {}, \n Father Name: {}".format(name, fname)  #format function


# In[76]:


"Name: {1}, \n Father Name: {0}".format(name, fname) #indexing change - direct index call


# In[77]:


"Name: {sn}, \n Father Name: {fn}".format(sn=name, fn=fname) #naming index - calling by name


# In[79]:


a=input("Enter your name ") #input from user
print(a)


# In[ ]:




