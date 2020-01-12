#!/usr/bin/env python
# coding: utf-8

# In[16]:


#First Question
marks = input("Enter Your Marks ")
if marks >= str(90):
    print("Grade A")
elif marks > str(80):
    print("Grade B")
elif marks > str(70):
    print("Grade C")
elif marks > str(60):
    print("Grade D")
else:
    print("Grade E")


# In[41]:


#Second Question

cost = 1.59
ret= 6
scr= True
day= "Sunday"
if ret > 8:
    print("You are charged for an extra day - cost " + str(cost*2))
    if scr == True:
        print("You are charged for scratch - cost " + str(cost+1))
elif day == "Sunday":
    print("You get 30% off - cost " + str(cost-0.3))
    if scr == True:
        print("You are charged for scratch - cost " + str(cost+2))
elif day == Thursday:
    print("You get 50% off - cost " + str(cost-0.5))
    
else:
    print("Ho")


# In[6]:


num=[0,1,2,3,4,5,6,7,8,9]
ind=0
while ind < 10:
    if ind==6:
        print("found")
        break
    else:
        ind+=1
   
    
print(ind)


# In[ ]:




