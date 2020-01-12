#!/usr/bin/env python
# coding: utf-8

# In[1]:


#for

for i in range (1,3):
    print("Pakistan", i)


# In[17]:


#for


for i in range (1000,990, -1):
   
    print(i)
    


# In[16]:


#Task 1
x=1000
while x>990:
    print(x)
    x -=1


# In[37]:


#Task 2
for i in range (65, 90):
    ch = chr(i)
    print (i, "=", ch)
    


# In[42]:


#Task 3 print row and column if divides by 5
l=[[2,5,9],
   [8, 9, 10],
   [20, 30, 27],
   [35, 9, 20]]

for ri, r in enumerate(l):
    for ci, c in enumerate(r):
        if c%5==0:
            print(ri, ci, c, end=" ")
    print()


# In[45]:


#Task 4 

ask = input("Enter Your Number: ")


for i in range (1,len(ask)):
    print(len(ask), "X" ,i, "=", len(ask)*i)


# In[47]:


#Task marketing example

initiative = 'You' #friend or girl
rich = True
slap = False
if initiative == 'You':
    if rich == True and slap == True:
        print('Customer Feedback')
    elif rich== True and slap ==  False:
        print('Direct Marketing')
    elif husband == True:
        print('Demand Supply Gap')
    
elif intiative == 'Friend':
    if friend == True:
        print('Thats advertising')
    
elif initiative == 'Girl':
    if rich == True:
        print('Brand Recognition')


# In[ ]:




