#!/usr/bin/env python
# coding: utf-8

# In[3]:


dir(list)


# In[2]:


#       0   2   3   4  5  6
names=["A", "B", "C", 7, 8, 9]

#slicing       
print(names[2])


# In[4]:


#Append
names = []
names.append("A")
names.append("B")
names.append("C")

names


# In[5]:


#Clear ( removes permanent)
names =[]

names.append("A")
names.append("B")
names.append("C")

names.clear()
names


# In[7]:


#Copy
names = []

names.append("A")
names.append("B")
names.append("C")

names1 = names #two varaibles with same list
print(names1)
print(names)

names1 [0] = 'Z' #update both lists - Shallow copy

print(names1)
print(names)


# In[8]:


#Copy
names = []

names.append("A")
names.append("B")
names.append("C")

names1 = names.copy() #two varaibles with same list
print(names1)
print(names)

names1 [0] = 'Z' #update only 1 lists - Deep copy

print(names1)
print(names)


# In[10]:


#Count
names =['A', 'B', 'A', 'C', 'B']
names.count("A")


# In[16]:


#Simple Extension
l1= ['A', 'B', 'C']
l2= ['X', 'Y', 'Z']

l3 = l1+l2 # it returns the value (inline fucntion - l1 l2 remains same)
print(l3)
print(l1)
print(l2)


# In[18]:


#Extend
l1= ['A', 'B', 'C']
l2= ['X', 'Y', 'Z']

l3=l1.extend(l2) # no value return. only extended in l1. (In memory operation)
print(l3)
print(l1)


# In[19]:


#index

print(l1)
l1.index("C")


# In[21]:


l1= ['A', 'B', 'C', 'A', 'X', 'Y', 'Z']
print(l1)
l1.index("A") #resturn first index


# In[23]:


l1= ['A', 'B', 'C', 'A', 'X', 'Y', 'Z']
print(l1)
print(l1.index("A"))
print(l1.index("A", 1)) #starting from 1 index - position based - always returns positive


# In[26]:


#Append
= []
#l1.append() #append at end of list
l1.insert(0, 'A') #insert at any index
l1.insert(0, 'B')
l1.insert(0, 'C')

print(l1)
#in append A,B,C
l1.insert(1, 'D') # insert at position 1
print(l1)


# In[27]:


#Pop
l1 = ['A', 'B', 'C']
a=l1.pop()  #removes from end by default - can take index -  stores in other varaibe, Return function
print(l1)
print(a)


# In[31]:


#Delete
l1 = ['A', 'B', 'C']
del l1[0] #delete never return value
print(l1)


# In[33]:


#Pop (using index)
l1 = ['A', 'B', 'C']
a=l1.pop(1) # removes from index
print(l1)
print(a)


# In[39]:


#Remove (by text value, not from index)
l1 = ['A', 'B', 'C', 'C','D', 'C']
print(l1)
l1.remove("C") #removes first value
print(l1)
l1.remove("C") #removes first value
print(l1)


# In[40]:


#Reverse (only reverse - no sorting)
l1= ['A', 'B', 'X', 'D', 'B', 'F', 'C']
l1.reverse()
print(l1)


# In[42]:


#Sort (Ascending by default)
l1= ['A', 'B', 'X', 'D', 'B', 'F', 'C']
print(l1)
l1.sort()
print(l1)


# In[43]:


#Sort for Descending
l1= ['A', 'B', 'X', 'D', 'B', 'F', 'C']
print(l1)
l1.sort()
l1.reverse()
print(l1)


# In[44]:


l1= ['A', 'B', 'X', 'D', 'B', 'F', 'C']
print(l1)
l1.sort(reverse= True)
print(l1)


# In[45]:


#Add (in line operation)
l1= ['A', 'B', 'C']
l1.__add__(['D', 'E']) # no updation in real data


# In[46]:


#Class
l1= ['A', 'B', 'C'] #it is list
l1.__class__


# In[47]:


#Contains  (returns either true or false - exist in list or not)
l1= ['A', 'B', 'C']
print(l1.__contains__("A"))
print(l1.__contains__("F"))


# In[48]:


#Equality
l1= ['A', 'B', 'C']
l2= ['A', 'B', 'C']
l3= ['D', 'E']
print(l1.__eq__(l2))
print(l1.__eq__(l3))


# In[50]:


#Greater than or Equal Comparison
l1= [5, 7, 9]
l2= [3, 6, 5]
l3=[7, 9, 10]

print(l1.__ge__(l2))
print(l1.__ge__(l3))


# In[51]:


#length function
print(len(l1))
print(l1.__len__())


# # Loops

# In[53]:


['Pakistan']*3


# In[54]:


#counter - Logic - inc/dec 
1 while
2 for


# In[55]:


#while

counter = 1

while counter <= 3:
    print("Pakistan", counter)
    counter +=1


# In[ ]:


#while

counter = 1

while counter >= 5:
    print("Pakistan", counter)
    counter -=1


# In[59]:


#for

for i in range (1,3):
    print("Pakistan", i)


# In[ ]:


["Pakistan"+str(x) for x in range (1,4)]


# In[ ]:




